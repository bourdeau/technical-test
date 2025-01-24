import os
import click
from dataclasses import dataclass
import requests

@dataclass
class ImageDataSource:
    path: str
    source_type: str
    format: str | None = None
    raw_data: str | None = None
    data: str | None = None

def get_path_types(paths: list[str]) -> list[ImageDataSource]:
    images_data = []

    for file_path in paths:
        file_path = file_path.strip()

        if file_path.startswith("http"):
            source_type = "http"
        elif os.path.isfile(file_path):
            source_type = "file"
        else:
            raise ValueError(f"Invalid file path: {file_path}")
    
        images_data.append(ImageDataSource(path=file_path, source_type=source_type))

    return images_data


def get_http_data(image: ImageDataSource):
    try:
        r = requests.get(image.path)

        if r.status_code != requests.codes.ok:
            raise Exception(f"HTTP error for {image.path}")

    except Exception:
        raise ValueError(f"HTTP error for {image.path}")

    return r.text.splitlines()

def get_file_data(image: ImageDataSource):
    with open(image.path, "r") as f:
        return f.read().splitlines()

def get_data(images: list[ImageDataSource]):
    data = None

    for image in images:
        if image.source_type == "http":
            data = get_http_data(image)
        if image.source_type == "file":
            data = get_file_data(image)
        
        image.raw_data = data

    return images

def image_type_guesser(images: list[ImageDataSource]):
    for image in images:
        # We only have one line so it's a line format
        if len(image.raw_data) == 1:
            image.format = "line"
        else:
            image.format = "table"

    return images

def image_formater(images: list):
    for image in images:
        if image.format == "line":
            image.data = format_line(image.raw_data)
        else:
            image.data = format_table(image.raw_data)

    return images

def format_table(raw_data):
    data = [[int(y) for y in x.split()] for x in raw_data if x]

    if len(set(len(n) for n in data)) != 1:
        raise Exception("The data is not in a valid table format")

    return data

def format_line(raw_data):
    row = raw_data[0]
    elements = row.split()
    nb_rows = int(elements[0])
    
    elements.pop(0)

    if len(elements) % nb_rows != 0:
        raise Exception("The data is not in a valid line format")
    
    nb_cols = len(elements) // nb_rows
    
    res = []
    for i in range(nb_rows):
        res.append([int(x) for x in elements[i * nb_cols:(i + 1) * nb_cols]])

    return res

def process_operation(images: list, operation: str):
    num_rows = len(images[0].data)
    if not all(len(image.data) == num_rows for image in images):
        raise ValueError("All images must have the same number of rows.")
    
    if operation == "APPEND":
        result = []
        for image in images:
            result.extend(image.data)
        return result

    elif operation == "COMBINE":
        result = []
        for row_idx in range(num_rows):
            combined_row = []
            for image in images:
                combined_row.extend(image.data[row_idx])
            result.append(combined_row)
        return result
    
    elif operation == "SUM":
        result = []
        for row_idx in range(num_rows):
            sum_row = []
            for col_idx in range(len(images[0].data[row_idx])):
                sum_row.append(sum(image.data[row_idx][col_idx] for image in images))
            result.append(sum_row)
        return result
    
    else:
        raise ValueError(f"Unsupported operation: {operation}")

@click.command()
@click.option('-p','--paths', help='URLs and/or file paths')
@click.option('-o','--operation', help='Operation to perform on the data')
def main(paths: str, operation: str):
    if operation not in ("APPEND", "COMBINE", "SUM"):
        raise ValueError(f"Invalid operation: {operation}")
    
    path_list = paths.split(',') if paths else []
    
    if not path_list:
        raise ValueError("--paths doesn't contain paths")
    
    # First we need to detect if it's a file or URLs
    res = get_path_types(path_list)
    res = get_data(res)
    res = image_type_guesser(res)
    res = image_formater(res)
    res = process_operation(res, operation)

    print(res)

if __name__ == "__main__":
    main()

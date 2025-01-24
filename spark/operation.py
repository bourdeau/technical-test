from typing import List
from spark.model import ImageData

class ImageOperation:
    """
    Handles operations (APPEND, COMBINE, SUM) on structured image data.

    Note: all operations are performed in the same method, we should
    probably have a method per operation as it is quite ugly.
    """

    @staticmethod
    def process(images: List[ImageData], operation: str) -> List[List[int]]:
        num_rows = len(images[0].data)
        if not all(len(image.data) == num_rows for image in images):
            raise ValueError("All images must have the same number of rows.")

        if operation == "APPEND":
            return [row for image in images for row in image.data]
        elif operation == "COMBINE":
            return [
                [value for image in images for value in image.data[row_idx]]
                for row_idx in range(num_rows)
            ]
        elif operation == "SUM":
            return [
                [sum(image.data[row_idx][col_idx] for image in images) for col_idx in range(len(images[0].data[0]))]
                for row_idx in range(num_rows)
            ]
        else:
            raise ValueError(f"Unsupported operation: {operation}")
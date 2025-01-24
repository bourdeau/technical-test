from typing import List
from spark.model import ImageData

class ImageSerializer:
    """
    Deserializes the image data (line or table) into a structured format.
    
    Note: we could/should have a _to_line and _to_table methods to serialize the data back.
    I think that's what was asked, but I missed it.
    """

    @staticmethod
    def format(image: ImageData):
        """
        Simple factory method
        """
        if image.format == "line":
            image.data = ImageSerializer._from_line(image.raw_data)
        elif image.format == "table":
            image.data = ImageSerializer._from_table(image.raw_data)
        else:
            raise ValueError(f"Unknown format: {image.format}")

    @staticmethod
    def _from_table(raw_data: List[str]) -> List[List[int]]:
        data = [[int(x) for x in row.split()] for row in raw_data if row]
        
        if len(set(len(row) for row in data)) != 1:
            raise ValueError("Invalid table format")
        
        return data

    @staticmethod
    def _from_line(raw_data: List[str]) -> List[List[int]]:
        elements = raw_data[0].split()
        nb_rows = int(elements.pop(0))
        
        if len(elements) % nb_rows != 0:
            raise ValueError("Invalid line format")
        
        nb_cols = len(elements) // nb_rows
        
        return [[int(x) for x in elements[i * nb_cols:(i + 1) * nb_cols]] for i in range(nb_rows)]
from typing import List
from spark.model import ImageData

class ImageOperation:
    """
    Handles operations (APPEND, COMBINE, SUM) on structured image data.
    """
    images: List[ImageData]
    operation: str
    nb_rows: int

    def __init__(self, images: List[ImageData], operation: str):
        self.images = images
        self.operation = operation
        self.nb_rows = len(self.images[0].data)

    def process(self) -> List[List[int]]:
        
        if not all(len(image.data) == self.nb_rows for image in self.images):
            raise ValueError("All images must have the same number of rows.")
        
        if self.operation not in ["APPEND", "COMBINE", "SUM"]:
            raise ValueError(f"Unsupported operation: {self.operation}")

        if self.operation == "APPEND":
            return self._append(self.images)
        elif self.operation == "COMBINE":
            return self._combine(self.images)
        elif self.operation == "SUM":
            return self._sum(self.images)
        
    def _append(self, images: List[ImageData]) -> List[List[int]]:
        return [row for image in images for row in image.data]
    
    def _combine(self, images: List[ImageData]) -> List[List[int]]:
        return [
            [value for image in images for value in image.data[row_idx]]
            for row_idx in range(self.nb_rows)
        ]
    
    def _sum(self, images: List[ImageData]) -> List[List[int]]:
        """
        Note: this comprehension list is not very comprehensible which is sad.
        """
        return [
            [sum(image.data[row_idx][col_idx] for image in images) for col_idx in range(len(images[0].data[0]))]
            for row_idx in range(self.nb_rows)
        ]
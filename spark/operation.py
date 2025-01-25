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
        """
        Append the images by stacking their rows

        Example:
        Image 1: [[1, 2], [3, 4]]
        Image 2: [[5, 6], [7, 8]]
        Result: [[1, 2], [3, 4], [5, 6], [7, 8]]
        """
        return [row for image in images for row in image.data]
    
    def _combine(self, images: List[ImageData]) -> List[List[int]]:
        """
        Combine the images by stacking their columns

        Example:
        Image 1: [[1, 2], [3, 4]]
        Image 2: [[5, 6], [7, 8]]
        Result: [[1, 2, 5, 6], [3, 4, 7, 8]]
        """
        result = []

        for row_idx in range(self.nb_rows):
            row = []

            for image in images:
                for value in image.data[row_idx]:
                    row.append(value)

            result.append(row)

        return result
    
    def _sum(self, images: List[ImageData]) -> List[List[int]]:
        """
        Sum the images by adding their columns

        Example:
        Image 1: [[1, 2], [3, 4]]
        Image 2: [[5, 6], [7, 8]]
        Result: [[6, 8], [10, 12]]
        """
        result = []

        for row_idx in range(self.nb_rows):
            result.append([])
            
            for col_idx in range(len(images[0].data[0])):
                column_sum = 0

                for image in images:
                    column_sum += image.data[row_idx][col_idx]

                result[row_idx].append(column_sum)

        return result

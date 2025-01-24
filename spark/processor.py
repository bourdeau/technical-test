import os
from typing import List
from spark.model import ImageData
from spark.loader import ImageLoader
from spark.format import ImageFormatGuesser
from spark.serializer import ImageSerializer
from spark.operation import ImageOperation


class ImageProcessor:
    """
    Processes images from different sources (http & file) 
    and performs operations (APPEND, COMBINE & SUM) on them.
    """

    @staticmethod
    def run(paths: List[str], operation: str) -> List[List[int]]:
        """
        Performs the specified operation on the images from the given paths.
        """
        images = ImageProcessor._build_image_collection(paths)
        
        for image in images:
            # Note: I'm not very found of calling static methods each time,
            # but I didn't take the time to make a factory.
            ImageLoader.load(image)
            ImageFormatGuesser.guess_format(image)
            ImageSerializer.format(image)
        
        return ImageOperation.process(images, operation)

    @staticmethod
    def _build_image_collection(paths: List[str]) -> List[ImageData]:
        """
        Check the images paths and initialize the ImageData objects.
        """
        images = []

        for path in paths:
            path = path.strip()
            if path.startswith("http"):
                source_type = "http"
            elif os.path.isfile(path):
                source_type = "file"
            else:
                raise ValueError(f"Invalid path: {path}")
            
            images.append(ImageData(path=path, source_type=source_type))
        
        return images
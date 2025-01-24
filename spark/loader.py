import requests
from typing import List
from spark.model import ImageData


class ImageLoader:
    """
    Load the image data from a http source of a file.
    """

    @staticmethod
    def load(image: ImageData):
        if image.source_type == "http":
            image.raw_data = ImageLoader._load_from_http(image.path)
        elif image.source_type == "file":
            image.raw_data = ImageLoader._load_from_file(image.path)
        else:
            raise ValueError(f"Unsupported source type: {image.source_type}")

    @staticmethod
    def _load_from_http(url: str) -> List[str]:
        """
        Note: the catch on the Exception is too generic, it should catch the appropriate exceptions from requests.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text.splitlines()
        except Exception as e:
            raise ValueError(f"Error loading HTTP data from {url}: {e}")

    @staticmethod
    def _load_from_file(file_path: str) -> List[str]:
        """
        Note: I didn't handle any kind of exception here, so it might just poorly crash.
        """
        with open(file_path, "r") as f:
            return f.read().splitlines()
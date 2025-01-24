from spark.model import ImageData

class ImageFormatGuesser:
    """
    Guess the format of the image data (line or table) based on the raw data.

    Note: this is very simple, but we could imagine handling many other and more complex formats.
    """
    @staticmethod
    def guess_format(image: ImageData):
        """
        If it's not a line then it's a table... (no comment)
        """
        if len(image.raw_data) == 1:
            image.format = "line"
        else:
            image.format = "table"
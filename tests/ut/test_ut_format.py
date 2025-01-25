from spark.model import ImageData
from spark.format import ImageFormatGuesser


def test_ut_format_line():
    image = ImageData(
        path="path/to/image",
        source_type="file",
        raw_data=["2 111 222 333 444 555 666"]
    )
    
    ImageFormatGuesser.guess_format(image)
    assert image.format == "line"

def test_ut_format_table():
    image = ImageData(
        path="path/to/image",
        source_type="file",
        raw_data=["1 23 345", "567 678 789"]
    )
    
    ImageFormatGuesser.guess_format(image)
    assert image.format == "table"
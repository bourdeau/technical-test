from spark.serializer import ImageSerializer
from spark.model import ImageData


def test_ut_image_serializer_from_table():
    image = ImageData(
        path="/path/to/image.txt",
        source_type="file",
        format="table",
        raw_data=["1 2 3", "4 5 6"],
    )

    ImageSerializer.format(image)
    assert image.data == [[1, 2, 3], [4, 5, 6]]


def test_ut_image_serializer_from_line():
    image = ImageData(
        path="/path/to/image.txt",
        source_type="file",
        format="line",
        raw_data=["2 111 222 333 444 555 666"],
    )

    ImageSerializer.format(image)
    assert image.data == [[111, 222, 333], [444, 555, 666]]
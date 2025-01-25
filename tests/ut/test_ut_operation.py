from spark.operation import ImageOperation
from spark.model import ImageData

def test_ut_image_operation_append():
    images = [
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 111 222 333 444 555 666"],
            data=[[111, 222, 333], [444, 555, 666]]
        ),
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 777 888 999 000 111 222"],
            data=[[777, 888, 999], [000, 111, 222]]
        )
    ]
    operation = ImageOperation(images, "APPEND")
    assert operation.process() == [[111, 222, 333], [444, 555, 666], [777, 888, 999], [000, 111, 222]]

def test_ut_image_operation_combine():
    images = [
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 111 222 333 444 555 666"],
            data=[[111, 222, 333], [444, 555, 666]]
        ),
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 777 888 999 000 111 222"],
            data=[[777, 888, 999], [000, 111, 222]]
        )
    ]
    operation = ImageOperation(images, "COMBINE")
    assert operation.process() == [[111, 222, 333, 777, 888, 999], [444, 555, 666, 000, 111, 222]]

def test_ut_image_operation_sum():
    images = [
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 111 222 333 444 555 666"],
            data=[[111, 222, 333], [444, 555, 666]]
        ),
        ImageData(
            path="/path/to/image.txt",
            source_type="file",
            format="line",
            raw_data=["2 777 888 999 000 111 222"],
            data=[[777, 888, 999], [000, 111, 222]]
        )
    ]
    operation = ImageOperation(images, "SUM")
    assert operation.process() == [[888, 1110, 1332], [444, 666, 888]]
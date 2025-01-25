from spark.processor import ImageProcessor

def test_image_processor_append():
    paths = [
        "https://gist.githubusercontent.com/bourdeau/c215096bb45e1b3a4ce1a827bb091f2e/raw/037a1c1c4bb948c642027d778dfd2906c0160838/gistfile1.txt",
        "/home/ph/www/spark/tests/samples/test-line.txt"
    ]
    operation = "APPEND"
    result = ImageProcessor.run(paths, operation)

    expect = [[1, 23, 345], [567, 678, 789], [111, 222, 333], [444, 555, 666]]

    assert result == expect


def test_image_processor_combine():
    paths = [
        "https://gist.githubusercontent.com/bourdeau/c215096bb45e1b3a4ce1a827bb091f2e/raw/037a1c1c4bb948c642027d778dfd2906c0160838/gistfile1.txt",
        "/home/ph/www/spark/tests/samples/test-line.txt"
    ]
    operation = "COMBINE"
    result = ImageProcessor.run(paths, operation)

    expect = [[1, 23, 345, 111, 222, 333], [567, 678, 789, 444, 555, 666]]

    assert result == expect

def test_image_processor_sum():
    paths = [
        "https://gist.githubusercontent.com/bourdeau/c215096bb45e1b3a4ce1a827bb091f2e/raw/037a1c1c4bb948c642027d778dfd2906c0160838/gistfile1.txt",
        "/home/ph/www/spark/tests/samples/test-line.txt"
    ]
    operation = "SUM"
    result = ImageProcessor.run(paths, operation)

    expect = [[112, 245, 678], [1011, 1233, 1455]]

    assert result == expect

from unittest.mock import mock_open, patch
from spark.model import ImageData
from spark.loader import ImageLoader


@patch("builtins.open", mock_open(read_data="2 111 222 333 444 555 666"))
def test_load_from_file():
    image_data = ImageData(path="mock_file.txt", source_type="file")
    
    ImageLoader.load(image_data)
    
    assert image_data.raw_data == ["2 111 222 333 444 555 666"]


@patch("requests.get")
def test_load_from_http(mock_get):
    mock_get.return_value.text = "2 111 222 333 444 555 666"
    
    image_data = ImageData(path="http://mock_file.txt", source_type="http")
    
    ImageLoader.load(image_data)
    
    assert image_data.raw_data == ["2 111 222 333 444 555 666"]
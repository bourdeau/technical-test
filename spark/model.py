from dataclasses import dataclass
from typing import List

@dataclass
class ImageData:
    path: str
    source_type: str
    format: str | None = None
    raw_data: List[str] | None = None
    data: List[List[int]] | None = None

from dataclasses import dataclass


@dataclass
class Video:
    id: str
    quality: str
    destination: str

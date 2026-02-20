from dataclasses import dataclass

@dataclass
class ShipPlacement:
        orientation: str
        row: int
        col: int


class InvalidPlacement(Exception):
    pass
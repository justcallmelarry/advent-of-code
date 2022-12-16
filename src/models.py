"""
Common models for stuff that seems recurring over the years
"""

from dataclasses import dataclass


@dataclass
class Coords:
    name: str = ""
    x: int = 0
    y: int = 0

    @property
    def coords(self) -> tuple[int, int]:
        return self.x, self.y

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name} x={self.x} y={self.y})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name} x={self.x} y={self.y})"

"""
Common models for stuff that seems recurring over the years
"""

from dataclasses import dataclass


@dataclass
class Coords:
    name: str
    x: int = 0
    y: int = 0

    @property
    def current_pos(self) -> tuple[int, int]:
        return self.x, self.y

    def __str__(self) -> str:
        return f"Coords({self.name} x={self.x} y={self.y})"

    def __repr__(self) -> str:
        return f"Coords({self.name} x={self.x} y={self.y})"

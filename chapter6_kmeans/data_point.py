from __future__ import annotations

from math import sqrt
from typing import List, Tuple, Iterable


class DataPoint:
    def __init__(self, initial_dimensions: List[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial_dimensions)
        # dimensions are supposed to be replaced with z_scored original values
        self.dimensions: Tuple[float, ...] = tuple(initial_dimensions)

    def distance(self, other: DataPoint) -> float:
        pairs: Iterable[Tuple[float, float]] = zip(self.dimensions, other.dimensions)
        differences: List[float] = [(x - y) ** 2 for x, y in pairs]
        return sqrt(sum(differences))

    @property
    def num_dimensions(self) -> int:
        return len(self.dimensions)

    def __eq__(self, other) -> bool:
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self) -> str:
        return self._originals.__repr__()

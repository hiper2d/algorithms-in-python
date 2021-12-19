from __future__ import annotations

from math import sqrt
from typing import List, Tuple, Iterable


class DataPoint:
    def __init__(self, initial: List[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial)
        self.dimensions: Tuple[float, ...] = tuple(initial)

    def distance(self, other: DataPoint) -> float:
        pairs: Iterable[Tuple[float, float]] = zip(self.dimensions, other.dimensions)
        differences: List[float] = [(x - y)**2 for x, y in pairs]
        return sqrt(sum(differences))

    @property
    def num_dimensions(self) -> int:
        len(self.dimensions)

    def __eq__(self, other) -> bool:
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self) -> str:
        return self._originals.__repr__()

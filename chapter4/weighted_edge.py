from __future__ import annotations

from dataclasses import dataclass
from chapter4.edge import Edge


@dataclass(frozen=True, eq=True)
class WeightedEdge(Edge):
    weight: float

    def reversed(self) -> Edge:
        return WeightedEdge(self.v, self.u, self.weight)

    def __lt__(self, other: WeightedEdge):
        return self.weight < other.weight

    def __str__(self) -> str:
        return "{self.u} {self.weight}> {self.v}"




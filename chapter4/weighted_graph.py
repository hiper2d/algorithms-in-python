from typing import TypeVar, Generic, List, Tuple

from chapter4.graph import Graph
from chapter4.weighted_edge import WeightedEdge

V = TypeVar('V')


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []):
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float):
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V, weight: float):
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        edges: List[WeightedEdge] = self.edges_for_index(index)
        for e in edges:
            distance_tuples.append((self.vertex_at(e.v), e.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc






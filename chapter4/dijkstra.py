from __future__ import annotations


from dataclasses import dataclass
from typing import TypeVar, Tuple, List, Dict, Optional

from chapter4.weighted_edge import WeightedEdge
from chapter4.weighted_graph import WeightedGraph
from util.generic_search import PriorityQueue

V = TypeVar['V']


@dataclass
class DijkstraNode:
    vertex_index: int
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance


def dijkstra(wg: WeightedGraph[V], root: V) -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:
    starting_index: int = wg.index_of(root)
    distances: List[Optional[float]] = [None] * wg.vertex_count
    distances[0] = 0
    path_dict: Dict[int, WeightedEdge] = {}
    queue: PriorityQueue[DijkstraNode] = PriorityQueue()
    queue.push(DijkstraNode(starting_index, 0))

    while not queue.empty:
        current_node: DijkstraNode = queue.pop()
        u: int = current_node.vertex_index
        dist_u: float = distances[u]
        neighbours: List[WeightedEdge] = wg.edges_for_index(u)
        for edge in neighbours:
            dist_v = distances[edge.v]
            if dist_v is None or edge.weight + dist_u < dist_v:
                distances[edge.v] = edge.weight + dist_u
                path_dict[edge.v] = edge
                queue.push(DijkstraNode(edge.v, edge.weight + dist_u))

    return distances, path_dict

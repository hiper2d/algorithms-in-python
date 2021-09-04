from __future__ import annotations


from dataclasses import dataclass
from typing import TypeVar, Tuple, List, Dict, Optional

from chapter4.mst import WeightedPath, print_weighted_path
from chapter4.weighted_edge import WeightedEdge
from chapter4.weighted_graph import WeightedGraph
from util.generic_search import PriorityQueue

V = TypeVar('V')


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
    distances[starting_index] = 0
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


def distance_array_to_vertex_dict(wg: WeightedGraph, distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict


def path_dict_to_path(start: int, end: int, path_dict: Dict[int, WeightedEdge]) -> WeightedPath:
    if len(path_dict) < 1:
        return []
    path: WeightedPath = []
    current_edge = path_dict[end]
    path.append(current_edge)
    while current_edge.u != start:
        current_edge = path_dict[current_edge.u]
        path.append(current_edge)
    return list(reversed(path))


if __name__ == "__main__":
    city_graph3: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix",
                                                     "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas",
                                                     "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph3.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph3.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph3.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph3.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph3.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph3.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph3.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph3.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph3.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph3.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph3.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph3.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph3.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph3.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph3.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph3.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph3.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph3.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph3.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph3.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph3.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph3.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph3.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph3.add_edge_by_vertices("Boston", "New York", 190)
    city_graph3.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph3.add_edge_by_vertices("Philadelphia", "Washington", 123)

    distances, path = dijkstra(city_graph3, "Los Angeles")
    named_distances: Dict[str, Optional[float]] = distance_array_to_vertex_dict(city_graph3, distances)
    print("Distances from Los Angeles:")
    for k,v in named_distances.items():
        print(f"{k} : {v}")
    print("")

    print("Shortest path from Los Angeles to Boston:")
    u: int = city_graph3.index_of("Los Angeles")
    v: int = city_graph3.index_of("Boston")
    path_from_la_to_boston: WeightedPath = path_dict_to_path(u, v, path)
    print_weighted_path(city_graph3, path_from_la_to_boston)



import unittest

from chapter4.dijkstra import dijkstra
from chapter4.weighted_graph import WeightedGraph


class TestDijkstra(unittest.TestCase):

    def setUp(self) -> None:
        self.city_graph3: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix",
                                                         "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas",
                                                         "Houston", "Detroit", "Philadelphia", "Washington"])
        self.city_graph3.add_edge_by_vertices("Seattle", "Chicago", 1737)
        self.city_graph3.add_edge_by_vertices("Seattle", "San Francisco", 678)
        self.city_graph3.add_edge_by_vertices("San Francisco", "Riverside", 386)
        self.city_graph3.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
        self.city_graph3.add_edge_by_vertices("Los Angeles", "Riverside", 50)
        self.city_graph3.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
        self.city_graph3.add_edge_by_vertices("Riverside", "Phoenix", 307)
        self.city_graph3.add_edge_by_vertices("Riverside", "Chicago", 1704)
        self.city_graph3.add_edge_by_vertices("Phoenix", "Dallas", 887)
        self.city_graph3.add_edge_by_vertices("Phoenix", "Houston", 1015)
        self.city_graph3.add_edge_by_vertices("Dallas", "Chicago", 805)
        self.city_graph3.add_edge_by_vertices("Dallas", "Atlanta", 721)
        self.city_graph3.add_edge_by_vertices("Dallas", "Houston", 225)
        self.city_graph3.add_edge_by_vertices("Houston", "Atlanta", 702)
        self.city_graph3.add_edge_by_vertices("Houston", "Miami", 968)
        self.city_graph3.add_edge_by_vertices("Atlanta", "Chicago", 588)
        self.city_graph3.add_edge_by_vertices("Atlanta", "Washington", 543)
        self.city_graph3.add_edge_by_vertices("Atlanta", "Miami", 604)
        self.city_graph3.add_edge_by_vertices("Miami", "Washington", 923)
        self.city_graph3.add_edge_by_vertices("Chicago", "Detroit", 238)
        self.city_graph3.add_edge_by_vertices("Detroit", "Boston", 613)
        self.city_graph3.add_edge_by_vertices("Detroit", "Washington", 396)
        self.city_graph3.add_edge_by_vertices("Detroit", "New York", 482)
        self.city_graph3.add_edge_by_vertices("Boston", "New York", 190)
        self.city_graph3.add_edge_by_vertices("New York", "Philadelphia", 81)
        self.city_graph3.add_edge_by_vertices("Philadelphia", "Washington", 123)
        self.distances, self.path = dijkstra(self.city_graph3, "Los Angeles")

    def test_neighbors_for_index_with_weights(self):
        expected_distance_from_la_to_boston: int = 2605
        actual_distance_from_la_to_boston = self.distances[self.city_graph3.index_of("Boston")]
        self.assertEqual(expected_distance_from_la_to_boston, actual_distance_from_la_to_boston)


if __name__ == '__main__':
    unittest.main()
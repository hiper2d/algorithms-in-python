import unittest
from typing import List, Tuple

from chapter4.weighted_graph import WeightedGraph


class TestGraphMethods(unittest.TestCase):

    def setUp(self) -> None:
        self._graph = WeightedGraph(['A', 'B', 'C'])
        self._graph.add_edge_by_indices(0, 1, 1.0)
        self._graph.add_edge_by_vertices('B', 'C', 2.0)

    def test_neighbors_for_index_with_weights(self):
        tested_tuple: List[Tuple[str, float]] = self._graph.neighbors_for_index_with_weights(1)
        expected_tuples = [('A', 1.0), ('C', 2.0)]
        self.assertEqual(tested_tuple, expected_tuples)

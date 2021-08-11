import unittest
from typing import List, Set

from chapter4.edge import Edge
from chapter4.graph import Graph


class TestGraphMethods(unittest.TestCase):

    # Graph with 3 vertices: A <-> B <-> C, A <-> D, A <-> C
    # A-D
    # |\
    # B-C
    def setUp(self) -> None:
        self._graph = Graph(['A', 'B', 'C'])
        self._graph.add_edge(Edge(0, 1))  # A <-> B
        self._graph.add_edge(Edge(1, 2))  # B <-> C
        self._graph.add_vertex('D')
        self._graph.add_edge_by_indices(0, 3)  # A <-> D
        self._graph.add_edge_by_vertices('A', 'C')  # A <-> C

    def test_counts(self):
        expected_vertex_count = 4
        expected_edge_count = 8
        self.assertEqual(expected_vertex_count, self._graph.vertex_count)
        self.assertEqual(expected_edge_count, self._graph.edge_count)

    def test_neighbors(self):
        self.assertSetEqual({'B', 'C', 'D'}, set(self._graph.neighbors_for_index(0)))
        self.assertSetEqual(({'A', 'C'}), set(self._graph.neighbors_for_vertex('B')))

    def test_edge_eq_and_hash(self):
        self.assertEqual(Edge(0, 1), Edge(0, 1))
        self.assertEqual(Edge(0, 1).__hash__(), Edge(0, 1).__hash__())
        self.assertTrue(Edge(0, 1).__eq__(Edge(0, 1)))
        self.assertSetEqual({Edge(0, 1), Edge(0, 2)}, {Edge(0, 2), Edge(0, 1)})

    def test_edges_for_methods(self):
        a_edges: Set[Edge] = {Edge(0, 1), Edge(0, 2), Edge(0, 3)}
        self.assertSetEqual(a_edges, set(self._graph.edges_for_index(0)))
        self.assertSetEqual(a_edges, set(self._graph.edges_for_vertex('A')))


if __name__ == '__main__':
    unittest.main()
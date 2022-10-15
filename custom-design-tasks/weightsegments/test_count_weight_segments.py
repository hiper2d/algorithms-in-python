from unittest import TestCase

from weightsegments.count_weight_segments import Solution


class TestSolution(TestCase):
    def test_count_valid_segments(self):
        self.assertEqual(5, Solution.count_valid_segments([1, 2, 8], 6))

import math
import unittest
from typing import List


class Solution:

    @staticmethod
    def find_max_median_sum(values: List[int], amount: int) -> int:
        medians = []
        curr = len(values) - 1
        while curr > len(values) - amount:
            medians.append(values[curr])
            curr -= 1

        mid = curr // 2
        rest_len = len(values[:curr+1])
        if rest_len % 2 == 0:
            medians.append(math.ceil((values[mid] + values[mid+1]) / 2))
        else:
            medians.append(values[mid])
        return sum(medians)


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    def testSolution(self):
        self.assertEqual(8, Solution.find_max_median_sum([1, 2, 3, 4, 5], 2))
# There is an array of numbers, the length of future sub-arrays and a threshold for these sub-arrays. The threshold
# is the difference between min and max items in a sub-array. Find the max number of sub-arrays that ben be built from
# the initial array withing the threshold restrictions.
import unittest
from typing import List


class Solution:
    @staticmethod
    def find_subarrays_number_with_threshold(arr: List[int], sub_arr_len: int, threshold: int) -> int:
        arr.sort() # 1, 3, 3, 4, 5, 6
        res = 0
        i = 0
        while i < len(arr) - sub_arr_len + 1:
            if arr[i + sub_arr_len - 1] - arr[i] <= threshold:
                res += 1
                i += sub_arr_len
            else:
                i += 1

        return res


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution.find_subarrays_number_with_threshold([3, 4, 3, 1, 6, 5], 3, 2))

    def test_solution_with_large_threshold(self):
        self.assertEqual(2, Solution.find_subarrays_number_with_threshold([3, 4, 3, 1, 6, 5], 3, 200))

    def test_solution_with_zero_threshold(self):
        self.assertEqual(0, Solution.find_subarrays_number_with_threshold([3, 4, 3, 1, 6, 5], 3, 0))

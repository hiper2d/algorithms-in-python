# You have an array. You are allowed to take any sub-array from it and calculate a sum out of it in the following way:
# - For each i-th item in the subarray (let's call it sub(i)) you can get a value from 1 to sub(n) inclusive. Let's call it sub_less(i).
# - Each of these values should meet the condition: sub_less(i) < sub_less(i+1)
# Find max sum which can be calculated this way.
# Example:
# Given [4, 5, 2, 3]
# Consider the sub-array [4, 5], it can give you the sum equals to 9. This is the max sum for the given array.

from unittest import TestCase
from typing import List


class Solution:
    @staticmethod
    def find_max_sum(arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        sums = []
        for end in range(len(arr)-1, 0, -1):
            curr = arr[end]
            sum = curr
            for i in range(end-1, -1, -1):
                if arr[i] >= curr:
                    curr = curr - 1
                    sum += curr
                else:
                    if curr > 1:
                        sum += arr[i]
                        curr = arr[i]
                    else:
                        sum += 1
                        break
            sums.append(sum)
        return max(sums)


class SolutionTest(TestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_solution(self):
        self.assertEqual(9, Solution.find_max_sum([4, 5, 2, 3]))
        self.assertEqual(12, Solution.find_max_sum([7, 4, 5, 2, 6, 5]))
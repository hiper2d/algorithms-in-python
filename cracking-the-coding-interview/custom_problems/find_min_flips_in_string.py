# Given a sequence of 'X' and 'Y' characters. You can flip 'X' with 'Y' and vise verse.
# Find the min number of flips to get the 'XX..YY' sequence.
import unittest


class Solution:
    @staticmethod
    def find_min_flips(s: str):
        x_count = 0
        y_count = 0
        for i in s:
            if i == 'X':
                x_count += 1
            else:
                y_count += 1
        left = 0
        curr_x_count = 0
        flips = 0
        while curr_x_count < x_count:
            if s[left] != 'X':
                s = s[:left] + 'X' + s[left+1:]
                x_count += 1
                y_count -= 1
                flips += 1
            curr_x_count += 1
            left += 1
        return flips


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1, Solution.find_min_flips('XXXXXYXYY'))

    def test_solution2(self):
        self.assertEqual(2, Solution.find_min_flips('YXXXXYXYY'))

    def test_solution3(self):
        self.assertEqual(1, Solution.find_min_flips('XXYYYYYYX'))
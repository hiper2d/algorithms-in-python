import math
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Testcase:
    n: int
    q: int
    t_sum_x: int
    t_sum_sqr_x: int
    t_sum_y: int
    t_sum_sqr_y: int
    w_sum_x: int
    w_sum_sqr_x: int
    w_sum_y: int
    w_sum_sqr_y: int


def read_int(file):
    return int(file.readline().strip())


def read_array_of_str(file):
    return file.readline().strip().split()


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)
        self.sum_trees_x: int = 0
        self.sum_trees_y: int = 0

    def load_testcases(self, path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = read_int(f)
            for _ in range(testcase_num):
                n = read_int(f)

                t_sum_x = 0
                t_sum_sqr_x = 0
                t_sum_y = 0
                t_sum_sqr_y = 0
                for _ in range(n):
                    [a, b] = read_array_of_str(f)
                    x = int(a)
                    y = int(b)
                    t_sum_x += x
                    t_sum_sqr_x += pow(x, 2)
                    t_sum_y += y
                    t_sum_sqr_y += pow(y, 2)

                q = read_int(f)

                w_sum_x = 0
                w_sum_sqr_x = 0
                w_sum_y = 0
                w_sum_sqr_y = 0
                for _ in range(q):
                    [a, b] = read_array_of_str(f)
                    x = int(a)
                    y = int(b)
                    w_sum_x += x
                    w_sum_sqr_x += pow(x, 2)
                    w_sum_y += y
                    w_sum_sqr_y += pow(y, 2)

                testcase = Testcase(n, q, t_sum_x, t_sum_sqr_x, t_sum_y, t_sum_sqr_y, w_sum_x, w_sum_sqr_x, w_sum_y, w_sum_sqr_y)
                testcases.append(testcase)
        return testcases

    def create_output(self) -> List[str]:
        output: List[str] = []
        for i, t in enumerate(self.testcases):
            res = self.process_testcase(t)
            output.append(f"Case #{i+1}: {res}")
        return output

    @staticmethod
    def process_testcase(t: Testcase) -> int:
        s: int = 0

        x_sqr = int(t.n * t.w_sum_sqr_x + t.q * t.t_sum_sqr_x - 2 * t.t_sum_x * t.w_sum_x)
        y_sqr = int(t.n * t.w_sum_sqr_y + t.q * t.t_sum_sqr_y - 2 * t.t_sum_y * t.w_sum_y)
        s += x_sqr + y_sqr

        return s % 1_000_000_007


if __name__ == "__main__":
    solution = Solution('watering_well_chapter_2_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            f.write(o + '\n')


from functools import lru_cache
from typing import List


class Testcase:
    def __init__(self, i: int, n: int, r: int, c: int, a: int, b: int):
        self.i = i
        self.n = n
        self.r = r
        self.c = c
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Testcase(i={self.i}, n={self.n}, r={self.r}, c={self.c}, a={self.a}, b={self.b})"


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    @staticmethod
    def load_testcases(path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = int(f.readline().strip())
            for i in range(testcase_num):
                nk = f.readline().strip().split()
                r = int(nk[0])
                c = int(nk[1])
                a = int(nk[2])
                b = int(nk[3])
                testcase = Testcase(i+1, testcase_num, r, c, a, b)
                testcases.append(testcase)
        return testcases

    def create_output(self) -> List[str]:
        output: List[str] = []
        for i, t in enumerate(self.testcases):
            res = self.process_testcase(t)
            output.append(f"Case #{i+1}: {'YES' if res else 'NO'}")
        return output

    @staticmethod
    def process_testcase(t: Testcase) -> bool:
        # print(t)
        r, c, a, b = t.r, t.c, t.a, t.b
        return r > c


if __name__ == "__main__":
    solution = Solution('dim_sum_delivery_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            print(o)
            f.write(o + '\n')

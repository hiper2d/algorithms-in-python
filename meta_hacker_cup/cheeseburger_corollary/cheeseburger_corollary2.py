from functools import lru_cache
from typing import List


class Testcase:
    def __init__(self, i: int, n: int, a: int, b: int, c: int):
        self.i = i
        self.n = n
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"Testcase(i={self.i}, n={self.n}, a={self.a}, b={self.b}, c={self.c})"


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
                s = int(nk[0])
                d = int(nk[1])
                k = int(nk[2])
                testcase = Testcase(i+1, testcase_num, s, d, k)
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
        # print(t)
        i, a, b, c = t.i, t.a, t.b, t.c

        if c < a and c < b:
            return 0

        if 2*a <= b:
            ans, rem = divmod(c, a)
        else:
            ans, rem = divmod(c, b)
            ans *= 2
            if rem < min(a, b):
                ans -= 1
            else:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution('cheeseburger_corollary_2_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            print(o)
            f.write(o + '\n')

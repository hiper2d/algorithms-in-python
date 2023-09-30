from typing import List


class Testcase:
    def __init__(self, i: int, n: int, s: int, d: int, k: int):
        self.i = i
        self.n = n
        self.s = s
        self.d = d
        self.k = k

    def __repr__(self):
        return f"Testcase(i={self.i}, n={self.n}, s={self.s}, d={self.d}, k={self.k})"


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
            output.append(f"Case #{i+1}: {'YES' if res else 'NO'}")
        return output

    @staticmethod
    def process_testcase(t: Testcase) -> bool:
        print(t)
        s, d, k = t.s, t.d, t.k
        buns = 2 * s + 2 * d
        patties = s + 2 * d
        # print(f"buns: {buns}, patties: {patties}, k: {k}, ans: {patties >= k and patties <= buns - 1}")
        return patties >= k and k <= buns - 1


if __name__ == "__main__":
    solution = Solution('cheeseburger_corollary_1_input_submit.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            print(o)
            f.write(o + '\n')
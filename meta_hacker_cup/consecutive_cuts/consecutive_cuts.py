from typing import List


class Testcase:
    def __init__(self, n: int, k: int, a: List[str], b: List[str]):
        self.n = n
        self.k = k
        self.a: List[str] = a
        self.b: List[str] = b


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    @staticmethod
    def load_testcases(path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = int(f.readline().strip())
            for _ in range(testcase_num):
                nk = f.readline().strip().split()
                n = int(nk[0])
                k = int(nk[1])
                a = f.readline().strip().split()
                b = f.readline().strip().split()
                testcase = Testcase(n, k, a, b)
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
        a_joined = ''.join(t.a)
        b_joined = ''.join(t.b)
        # if same then any k works except k == 1
        if a_joined == b_joined:
            return True if t.k != 1 else False
        # if reversed and len == 2 then only odd k works
        if len(a_joined) == 2 and a_joined == b_joined[::-1]:
            return True if t.k % 2 == 1 else False
        # in all other cases (b in a*2) works for all k > 0
        c = a_joined * 2
        return True if b_joined in c and t.k > 0 else False


if __name__ == "__main__":
    solution = Solution('consecutive_cuts_chapter_2_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            print(o)
            f.write(o + '\n')


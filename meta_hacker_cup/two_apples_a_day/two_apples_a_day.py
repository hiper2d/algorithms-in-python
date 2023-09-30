import heapq
from typing import List


def read_array_of_str(file) -> List[int]:
    str_arr = file.readline().strip().split()
    return list(map(lambda a: int(a), str_arr))


class Testcase:
    def __init__(self, i: int, n: int, a: List[int]):
        self.i = i
        self.n = n
        self.a = a

    def __repr__(self):
        return f"Testcase(i={self.i}, n={self.n}, a={self.a})"


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    @staticmethod
    def load_testcases(path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = int(f.readline().strip())
            for i in range(testcase_num):
                n = int(f.readline().strip())
                ass = read_array_of_str(f)
                testcase = Testcase(i+1, n, ass)
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
        i, arr, n = t.i, sorted(t.a), t.n
        s = sum(arr)

        if n == 1:
            return 1

        candidates = []
        candidate_to_sumpair = {}
        for a in arr:
            rest_sum = s - a
            pair_sum, mod = divmod(rest_sum, n-1)
            if a in candidate_to_sumpair:
                continue
            if mod == 0:
                lo, hi = 0, len(arr)-1
                is_candidate = True
                removed_candidate = False
                while lo < hi:
                    if arr[lo] == a and not removed_candidate:
                        lo += 1
                        removed_candidate = True
                    if arr[hi] == a and not removed_candidate:
                        hi -= 1
                        removed_candidate = True
                    if arr[lo] + arr[hi] != pair_sum:
                        is_candidate = False
                        break
                    lo += 1
                    hi -= 1
                if is_candidate:
                    candidates.append(-a)
                    candidate_to_sumpair[a] = pair_sum
        heapq.heapify(candidates)
        # print(i, arr, candidates, candidate_to_sumpair)

        if not candidates:
            return -1

        prev = -1
        while candidates:
            candidate = -heapq.heappop(candidates)
            if candidate == prev:
                continue
            prev = candidate
            pair_sum = candidate_to_sumpair[candidate]
            if pair_sum - candidate == 0:
                continue
            return pair_sum - candidate
        return -1


if __name__ == "__main__":
    solution = Solution('two_apples_a_day_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            print(o)
            f.write(o + '\n')

import re
import string
from collections import defaultdict
from dataclasses import dataclass
from typing import List


@dataclass
class Testcase:
    counter: int


def read_int(file):
    return int(file.readline().strip())


def read_array_of_str(file):
    return file.readline().strip().split()


def build_prefix_sum(s: str) -> List[List[int]]:
    n = len(s)
    prefix_sum = [[0]*26 for _ in range(n+1)]
    for i in range(1, n+1):
        for j, c in enumerate(string.ascii_lowercase):
            prefix_sum[i][j] = prefix_sum[i-1][j]
            if s[i-1] == c:
                prefix_sum[i][j] += 1
    return prefix_sum


class Solution:
    def __init__(self, input_path: str):
        self.memo = {}
        self.almost_memo = {}
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    def load_testcases(self, path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = read_int(f)
            for _ in range(testcase_num):
                template = f.readline().strip()
                n = len(template)
                q_count = read_int(f)
                counter = 0
                for _ in range(q_count):
                    [l_str, r_str] = read_array_of_str(f)
                    l = int(l_str)
                    r = int(r_str)
                    q_len = r - l + 1
                    q = template[l-1:r]
                    prefix_sum = build_prefix_sum(q)
                    if self.process_testcase(q, q_len, prefix_sum):
                        counter += 1
                testcase = Testcase(counter)
                testcases.append(testcase)
        return testcases

    def create_output(self) -> List[str]:
        output: List[str] = []
        for i, t in enumerate(self.testcases):
            output.append(f"Case #{i+1}: {t.counter}")
        return output

    def process_testcase(self, q, q_len, prefix_sum) -> bool:
        if q in self.memo:
            return self.memo[q]

        if q_len % 2 == 0:
            self.memo[q] = False
            return False
        mid = q_len // 2

        total_diff1 = 0
        total_diff2 = 0
        for j, c in enumerate(string.ascii_lowercase):
            left1 = prefix_sum[mid][j]
            right1 = prefix_sum[q_len][j] - prefix_sum[mid][j]
            left2 = prefix_sum[mid+1][j]
            right2 = prefix_sum[q_len][j] - prefix_sum[mid + 1][j]
            total_diff1 += abs(right1 - left1)
            total_diff2 += abs(right2 - left2)
            if total_diff1 > 1 and total_diff2 > 1:
                break
        if total_diff1 == 1 or total_diff2 == 1:
            self.memo[q] = True
            return True
        else:
            self.memo[q] = False
            return False


if __name__ == "__main__":
    solution = Solution('perfectly_balanced_chapter_1_validation_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            f.write(o + '\n')


from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def __init__(self):
        self.testcases: int = 0
        self.n: List[int] = []
        self.k: List[int] = []
        self.s: List[List[int]] = []

    def load_input(self, path: str):
        with open(path) as f:
            self.testcases = int(f.readline())
            for t in range(self.testcases):
                [n, k] = f.readline().split()
                self.n.append(int(n))
                self.k.append(int(k))
                ss = f.readline().split()
                self.s.append([int(s) for s in ss])

    def determine_output(self, i: int) -> str:
        n = self.n[i]
        k = self.k[i]
        s = self.s[i]
        unique_styles = len(set(s))
        m = defaultdict(int)
        for u in s:
            m[u] += 1
        max_per_stype = sorted(m.values())[-1]
        unique_per_case = ceil(unique_styles / 2)
        cases_needed_for_stypes = ceil(n / unique_styles)
        if n > k*2:
            return 'NO'
        if cases_needed_for_stypes > 2:
            return 'NO'
        if unique_per_case > k:
            return 'NO'
        if max_per_stype > 2:
            return 'NO'
        return 'YES'


if __name__ == "__main__":
    sol = Solution()
    sol.load_input('second_hands_input.txt')
    with open('output.txt', mode='w') as f:
        for i in range(1, sol.testcases+1):
            f.write(f"Case #{i}: {sol.determine_output(i-1)}\n")

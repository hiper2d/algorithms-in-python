import math
import sys
from dataclasses import dataclass
from typing import List, Set


@dataclass
class House:
    x: int
    y: int
    is_convex: bool
    is_start: bool
    is_end: bool
    damage: int = -1
    visited: bool = False

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@dataclass
class Testcase:
    n: int
    k: int
    d: int
    houses: List[House]


def read_int(file):
    return int(file.readline().strip())


def read_array_of_str(file):
    return file.readline().strip().split()


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    def load_testcases(self, path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = read_int(f)
            for _ in range(testcase_num):
                [n, k, d] = list(map(lambda a: int(a), read_array_of_str(f)))
                houses: List[House] = []
                for i in range(n):
                    [x, y] = read_array_of_str(f)
                    is_convex = True if i == 0 or i == n-1 else False
                    is_start = True if i == 0 else False
                    is_end = True if i == n - 1 else False
                    houses.append(House(int(x), int(y), is_convex, is_start, is_end))

                testcase = Testcase(n, k, d, houses)
                self.detect_convex_hull(testcase)
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
        convex_houses = [h for h in t.houses if h.is_convex and not h.is_start]
        start = t.houses[0]
        start.damage = 0
        start.visited = True
        target = t.houses[-1]

        def find_next(starting_house: House) -> List[House]:
            next_houses: List[House] = []
            for h in convex_houses:
                if not h.visited and Solution.dist(starting_house, h) < t.d:
                    next_houses.append(h)
            return next_houses

        def backtrack(current: House):
            if current == target:
                return
            next_houses = find_next(current)
            if not next_houses:
                return
            for next_house in next_houses:
                next_house_damage = current.damage + max(t.k, Solution.sqr_dist(current, next_house))
                if next_house.damage != -1 and next_house.damage < next_house_damage:
                    continue
                else:
                    next_house.damage = next_house_damage
                    next_house.visited = True
                    backtrack(next_house)
                    next_house.visited = False
        backtrack(start)
        return target.damage

    @staticmethod
    def detect_convex_hull(t: Testcase):
        """
        This method is super slow (n^2) and cannot handle the 'lemonade_life_input.txt' file
        Try this one (n*log(n)): https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
        """
        start = 0
        p = start
        while True:
            t.houses[p].is_convex = True
            q = (p + 1) % t.n
            for i in range(t.n):
                orientation = Solution.orientation(t.houses[p], t.houses[i], t.houses[q])
                if orientation == 2:
                    q = i
                elif orientation == 0:
                    # skip collinear, keep only furthest as convex
                    if Solution.furthest(t.houses[p], t.houses[i], t.houses[q]) == 1:
                        q = i
            p = q
            if p == start:
                break

    @staticmethod
    def orientation(p: House, q: House, r: House):
        """
        To find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are collinear
        1 --> Clockwise
        2 --> Counterclockwise
        """
        val = (q.y - p.y) * (r.x - q.x) - \
              (q.x - p.x) * (r.y - q.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    @staticmethod
    def dist(p: House, q: House):
        return math.sqrt(pow(q.y - p.y, 2) + pow(q.x - p.x, 2))

    @staticmethod
    def sqr_dist(p: House, q: House):
        return pow(q.y - p.y, 2) + pow(q.x - p.x, 2)

    @staticmethod
    def furthest(p: House, q: House, r: House):
        dist1 = Solution.sqr_dist(p, q)
        dist2 = Solution.sqr_dist(p, r)
        return 1 if dist1 > dist2 else -1


if __name__ == "__main__":
    solution = Solution('lemonade_life_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            f.write(o + '\n')

    # count = 0
    # with open('lemonade_life_input.txt') as f:
    #     for line in f:
    #         count += len(line)
    # print(count)

    #print(Solution.process_testcase(solution.testcases[0]))


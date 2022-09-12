import math
import sys
from dataclasses import dataclass
from functools import cmp_to_key
from typing import List, Set


@dataclass
class House:
    x: int
    y: int
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
    hull: List[House]
    target: House


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
                    houses.append(House(int(x), int(y)))

                hull = self.detect_convex_hull(houses)
                testcase = Testcase(n, k, d, hull, houses[-1])
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
        convex_houses = t.hull
        start = t.hull[0]
        start.damage = 0
        start.visited = True
        target = t.target

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
    def detect_convex_hull(houses: List[House]) -> List[House]:
        """
        This method is super slow (n^2) and cannot handle the 'lemonade_life_input.txt' file
        Try this one (n*log(n)): https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
        """
        p0 = houses[0]
        n = len(houses)

        def compare(p1: House, p2: House):
            o = Solution.vertical_orientation(p0, p1, p2)
            if o == 0:
                if Solution.sqr_dist(p0, p1) > Solution.sqr_dist(p0, p1):
                    return -1
                else:
                    return 1
            else:
                if o == 2:
                    return -1
                else:
                    return 1

        points = sorted(houses, key=cmp_to_key(compare))
        m = 1
        for i in range(1, n):
            while (i < n - 1) and Solution.vertical_orientation(p0, points[i], points[i+1]) == 0:
                i += 1
            points[m] = points[i]
            m += 1

        if m < 3:
            return [p0, houses[-1]]

        hull = []
        hull.extend(points[:3])
        for i in range(3, m):
            while len(hull) > 0 and Solution.vertical_orientation(hull[-2], hull[-1], points[i]) != 2:
                hull.pop()
            hull.append(points[i])
        return hull

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
    def vertical_orientation(p: House, q: House, r: House):
        """
        To find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are collinear
        1 --> Clockwise
        2 --> Counterclockwise
        """
        val = (q.x - p.x) * (r.y - q.y) - \
              (q.y - p.y) * (r.x - q.x)

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
    # print(solution.testcases[2].hull)
    # print(Solution.process_testcase(solution.testcases[2]))


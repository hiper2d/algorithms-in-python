from typing import List, Tuple

POSSIBLE = 'Possible'
IMPOSSIBLE = 'Impossible'
ROCK = '#'
TREE = '^'
EMPTY = '.'


class Testcase:
    def __init__(self, trees_str: List[str], has_at_least_one_tree: bool = False):
        self.has_at_least_one_tree = has_at_least_one_tree
        self.trees_str: List[str] = trees_str


def check_for_at_least_two_friends(tree: List[str], row: int, col: int) -> bool:
    max_row, max_col = len(tree)-1, len(tree[0])-1
    friends_count = 0
    if row < max_row and tree[row+1][col] != ROCK:
        friends_count += 1
    if row > 0 and tree[row-1][col] != ROCK:
        friends_count += 1
    if col < max_col and tree[row][col+1] != ROCK:
        friends_count += 1
    if col > 0 and tree[row][col-1] != ROCK:
        friends_count += 1
    return friends_count >= 2


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    def create_output(self) -> List[str]:
        output: List[str] = []
        for i, t in enumerate(self.testcases):
            res, new_tree = self.process_testcase(t)
            output.append(f"Case #{i+1}: {res}")
            if new_tree:
                output.extend(new_tree)
        return output

    @staticmethod
    def load_testcases(path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = int(f.readline().strip())
            for _ in range(testcase_num):
                [rows_str, _] = f.readline().split()
                rows = int(rows_str)
                trees_str: List[str] = []
                has_at_least_one_tree = False
                for i in range(rows):
                    row_from_file = f.readline().strip()
                    trees_str.append(row_from_file)
                    if TREE in row_from_file:
                        has_at_least_one_tree = True
                testcase = Testcase(trees_str, has_at_least_one_tree)
                testcases.append(testcase)
        return testcases

    @staticmethod
    def process_testcase(t: Testcase) -> Tuple[str, List[str]]:
        if not t.has_at_least_one_tree:
            return POSSIBLE, t.trees_str
        elif len(t.trees_str) == 1 or len(t.trees_str[0]) == 1:
            return IMPOSSIBLE, []
        else:
            for r in range(len(t.trees_str)):
                for c in range(len(t.trees_str[0])):
                    if t.trees_str[r][c] == TREE:
                        if not check_for_at_least_two_friends(t.trees_str, r, c):
                            return IMPOSSIBLE, []
                t.trees_str[r] = t.trees_str[r].replace(EMPTY, TREE)
            return POSSIBLE, t.trees_str


if __name__ == "__main__":
    solution = Solution('second_second_friend_input.txt')
    with open('output.txt', mode='w') as f:
        for o in solution.create_output():
            f.write(o + '\n')

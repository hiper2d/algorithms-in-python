from math import log2, ceil
from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    val: str = None
    left: 'Node' = None
    right: 'Node' = None


class Testcase:
    def __init__(self, n: int, first_word: str):
        self.n = n
        self.first_word: str = first_word


class Solution:
    def __init__(self, input_path: str):
        self.testcases: List[Testcase] = self.load_testcases(input_path)

    @staticmethod
    def load_testcases(path: str) -> List[Testcase]:
        testcases: List[Testcase] = []
        with open(path) as f:
            testcase_num = int(f.readline())
            for _ in range(testcase_num):
                n: int = int(f.readline().strip())
                first_word = f.readline().strip()
                testcase = Testcase(n, first_word)
                testcases.append(testcase)
        return testcases

    @staticmethod
    def build_prefix_tree(n: int) -> Node:
        root = Node(left=Node(val='.'), right=Node(val='-'))
        q = deque()
        q.extend([root.left, root.right])
        i = 1
        while i <= n:
            next_q = deque()
            while q:
                node: Node = q.pop()
                node.left = Node(val=f"{node.val}.")
                node.right = Node(val=f"{node.val}-")
                next_q.extend([node.left, node.right])
            q = next_q
            i += 1
        return root

    @staticmethod
    def solve(testcase: Testcase, root: Node):
        level = 1
        current_level = deque()
        current_level.extend([root.left, root.right])
        while level < ceil(log2(testcase.n))+1:
            next_level = deque()
            while current_level:
                node: Node = current_level.pop()
                if testcase.first_word.startswith(node.val):
                    continue
                next_level.extend([node.left, node.right])
            current_level = next_level
            level += 1
        words_taken = []
        while len(words_taken) < testcase.n-1:
            word = current_level.pop().val
            if word != testcase.first_word:
                words_taken.append(word)
        return words_taken


if __name__ == "__main__":
    solution = Solution('second_second_meaning_input.txt')
    tree = solution.build_prefix_tree(8)
    with open('output.txt', mode='w') as f:
        for i, t in enumerate(solution.testcases):
            f.write(f"Case #{i+1}:\n")
            for w in solution.solve(t, tree):
                f.write(w + '\n')
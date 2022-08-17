from collections import defaultdict
from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    val: int
    children: List['Node'] = field(default_factory=lambda: [])


if __name__ == "__main__":
    inp = [[4, 5], [1, 2], [3, 1], [1, 5]]
    memo = defaultdict(list)
    for a, b in inp:
        memo[a].append(b)
        memo[b].append(a)
    visited = set()
    print(memo)
    visited.add(1)
    root = Node(1)

    def build_tree(node: Node):
        for v in memo[node.val]:
            if v not in visited:
                node.children.append(Node(v))
                visited.add(v)
        for c in node.children:
            build_tree(c)

    build_tree(root)
    print(root)


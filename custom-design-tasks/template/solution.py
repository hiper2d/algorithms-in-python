from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Tuple, List, Dict


@dataclass
class Node:
    val: str = None
    rank: int = 0
    is_word: bool = False
    children: Dict[str, 'Node'] = field(default_factory=lambda: defaultdict())

    def __eq__(self, o: object) -> bool:
        return self.val == o.val


class PrefixTree:
    def __init__(self, root: Node):
        self.root: Node = root


class Autocomplete:
    def __init__(self, dictionary: Dict[str, int], inputs: List[str]):
        self.dictionary: Dict[str, int] = dictionary
        self.inputs: List[str] = inputs

    @staticmethod
    def parse_input(path: str) -> Tuple[Dict[str, int], List[str]]:
        with open(path) as f:
            n = int(f.readline().strip())
            m = int(f.readline().strip())
            dictionary: Dict[str, int] = {}
            inputs: List[str] = []
            for i in range(n):
                dictionary[f.readline().strip()] = i+1
            for i in range(m):
                inputs.append(f.readline().strip())
            return dictionary, inputs

    @staticmethod
    def build_prefix_tree(words: Dict[str, int]) -> Node:
        root = Node()
        for word in words:
            cur_node = root
            for index, c in enumerate(word):
                is_last_letter = index == len(word)-1
                if c not in cur_node.children:
                    new_node = Node(c)
                    cur_node.children[c] = new_node
                    cur_node = new_node
                else:
                    cur_node = cur_node.children[c]
                if is_last_letter:
                    cur_node.is_word = True
                    cur_node.rank = words[word]
        return root

    @staticmethod
    def search_in_tree(root: Node, input: str) -> List[str]:
        res: List[str] = []
        for index, c in enumerate(input):
            is_last_letter = index == len(input)-1
            if c not in root.children:
                res.append(f"no result")
            root = root.children[c]
            if is_last_letter:
                res.extend(Autocomplete.collect_all_vals_from_tree(root, input))
        return res

    @staticmethod
    def collect_all_vals_from_tree(root: Node, prefix: str) -> List[str]:
        q = deque()
        q.append((root, prefix))
        res: List[(str, int)] = []
        while q:
            node, prefix = q.pop()
            if node.is_word:
                res.append(f"{prefix} ({node.rank})")
            for c in node.children:
                q.append((node.children[c], prefix+node.children[c].val))
        return res


if __name__ == "__main__":
    auto = Autocomplete(*Autocomplete.parse_input('input.txt'))
    tree: Node = auto.build_prefix_tree(auto.dictionary)
    with open('output.txt', mode='w') as f:
        for word in auto.inputs:
            f.write(f"{word}:\n")
            for r in auto.search_in_tree(tree, word):
                f.write(f"{r}\n")
            f.write("\n")

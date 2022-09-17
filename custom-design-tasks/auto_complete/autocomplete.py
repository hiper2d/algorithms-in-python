from dataclasses import dataclass, field
from typing import List, Dict, Set


@dataclass
class TrieNode:
    is_word: bool = False
    children: Dict[str, 'TrieNode'] = field(default_factory=lambda: {})


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        curr: TrieNode = self.root
        for i, c in enumerate(word):
            is_last_letter = True if i == len(word) - 1 else False
            if c not in curr.children:
                new_node = TrieNode(is_last_letter)
                curr.children[c] = new_node
            curr = curr.children[c]

    def search(self, prefix: str) -> Set[str]:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return set()
            else:
                curr = curr.children[c]
        if curr.children:
            return self.traverse(curr, prefix)

    def traverse(self, curr: TrieNode, prefix: str) -> Set[str]:
        solutions = set()
        for c in curr.children:
            new_prefix = prefix + c
            if curr.children[c].is_word:
                solutions.add(new_prefix)
            solutions.update(self.traverse(curr.children[c], new_prefix))
        return solutions


class Autocomplete:
    def __init__(self):
        self.trie = Trie()

    def add_words_to_dictionary(self, words: List[str]):
        for word in words:
            self.trie.add(word)

    def autocomplete(self, prefix: str) -> Set[str]:
        return self.trie.search(prefix)

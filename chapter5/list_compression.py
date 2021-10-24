from __future__ import annotations

from copy import deepcopy
from pickle import dumps
from random import shuffle, sample
from sys import getsizeof
from typing import List, Tuple, Any, Type
from zlib import compress

# 165 bytes compressed
from chapter5.chromosome import Chromosome, T

PEOPLE: List[str] = ["Michael", "Sarah", "Joshua", "Narine", "David", "Sajid", "Melanie", "Daniel", "Wei", "Dean", "Brian", "Murat", "Lisa"]


class ListCompression(Chromosome):
    def __init__(self, lst: List[Any]):
        self.list: List[Any] = lst

    @property
    def bytes_compressed(self) -> int:
        return getsizeof(compress(dumps(self.list)))

    @classmethod
    def random_instance(cls: Type[ListCompression]) -> ListCompression:
        copy: List[str] = deepcopy(PEOPLE)
        shuffle(copy)
        return ListCompression(copy)

    def fitness(self: ListCompression) -> float:
        return 1 / self.bytes_compressed

    def crossover(self: ListCompression, other: ListCompression) -> Tuple[ListCompression, ListCompression]:
        child1: ListCompression = deepcopy(self)
        child2: ListCompression = deepcopy(other)
        i1, i2 = sample(range(len(self.list)), k=2)
        word1, word2 = child1.list[i1], child2.list[i2]
        word1_index_in_child2: int = child2.list.index(word1)
        word2_index_in_child1: int = child1.list.index(word2)
        child2.list[i1], child2.list[word1_index_in_child2] = word1, child2.list[i1]
        child1.list[i2], child1.list[word2_index_in_child1] = word2, child1.list[i2]
        return child1, child2

    def mutate(self: ListCompression) -> None:
        i1, i2 = sample(range(len(self.list)), k=2)
        self.list[i1], self.list[i2] = self.list[i2], self.list[i1]

    def __str__(self) -> str:
        return f"Order: {self.list}, bytes: {self.bytes_compressed}"


if __name__ == "__main__":
    initial_population: List[ListCompression] = [ListCompression.random_instance() for _ in range(1000)]
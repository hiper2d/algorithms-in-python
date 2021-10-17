from __future__ import annotations
from typing import List, Tuple, Any, Type

# 165 bytes compressed
from chapter5.chromosome import Chromosome, T

PEOPLE: List[str] = ["Michael", "Sarah", "Joshua", "Narine", "David", "Sajid", "Melanie", "Daniel", "Wei", "Dean", "Brian", "Murat", "Lisa"]


class ListCompression(Chromosome):
    def __init__(self, lst: List[Any]):
        self.lst: List[Any] = lst

    @classmethod
    def random_instance(cls: Type[T]) -> T:
        pass

    def fitness(self: T) -> float:
        pass

    def crossover(self: T, other: T) -> Tuple[T, T]:
        pass

    def mutate(self: T) -> None:
        pass
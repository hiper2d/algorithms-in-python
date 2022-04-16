from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Tuple

T = TypeVar('T', bound='Chromosome')


class Chromosome(ABC):
    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        ...

    @abstractmethod
    def fitness(self: T) -> float:
        ...

    @abstractmethod
    def crossover(self: T, other: T) -> Tuple[T, T]:
        ...

    @abstractmethod
    def mutate(self: T) -> None:
        ...

    def __gt__(self, other: Chromosome) -> bool:
        return self.fitness() > other.fitness()
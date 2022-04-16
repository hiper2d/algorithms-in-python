from __future__ import annotations

from copy import deepcopy
from random import shuffle, sample
from typing import Tuple, Type, List

from chapter5.chromosome import Chromosome, T
from chapter5.genetic_algorithm import GeneticAlgorithm


class SendMoreMoney2(Chromosome):
    def __init__(self, letters: List[str]):
        self.letters: List[str] = letters

    @classmethod
    def random_instance(cls: Type[SendMoreMoney2]) -> T:
        letters = ["S", "E", "N", "D", "M", "O", "R", "Y", " ", " "]
        shuffle(letters)
        return SendMoreMoney2(letters)

    def fitness(self: T) -> float:
        send, more, money, diff = self._get_diff()
        return 1 / (1 + diff)

    def crossover(self: SendMoreMoney2, other: SendMoreMoney2) -> Tuple[SendMoreMoney2, SendMoreMoney2]:
        child1: SendMoreMoney2 = deepcopy(self)
        child2: SendMoreMoney2 = deepcopy(self)
        idx1, idx2 = sample(range(len(self.letters)), k=2)
        l1, l2 = child1.letters[idx1], child2.letters[idx2]
        child1.letters[child1.letters.index(l2)], child1.letters[idx2] = child1.letters[idx2], l2
        child2.letters[child2.letters.index(l1)], child2.letters[idx1] = child2.letters[idx1], l1
        return child1, child2

    def mutate(self: SendMoreMoney2) -> None:
        idx1, idx2 = sample(range(len(self.letters)), k=2)
        self.letters[idx1], self.letters[idx2] = self.letters[idx2], self.letters[idx1]

    def __str__(self) -> str:
        send, more, money, diff = self._get_diff()
        return f"{send} + {more} = {money}, difference {diff}"

    def _get_diff(self) -> Tuple[int, int, int, int]:
        s: int = self.letters.index("S")
        e: int = self.letters.index("E")
        n: int = self.letters.index("N")
        d: int = self.letters.index("D")
        m: int = self.letters.index("M")
        o: int = self.letters.index("O")
        r: int = self.letters.index("R")
        y: int = self.letters.index("Y")
        send: int = 1000 * s + 100 * e + 10 * n + d
        more: int = 1000 * m + 100 * o + 10 * r + e
        money: int = 10_000 * m + 1000 * o + 100 * n + 10 * e + y
        diff: int = abs(money - (send + more))
        return send, more, money, diff


if __name__ == "__main__":
    initial_population: List[SendMoreMoney2] = [SendMoreMoney2.random_instance() for _ in range(1000)]
    ga: GeneticAlgorithm = GeneticAlgorithm(initial_population=initial_population, max_generations=1000,
                                            threshold=1.0, crossover_chance=.7, mutation_chance=.7,
                                            selection_type=GeneticAlgorithm.SelectionType.ROULETTE)
    result: SendMoreMoney2 = ga.run()
    print(result)
    # send = 3712
    # more = 0467
    # money = 04179


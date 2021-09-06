from __future__ import annotations

from copy import deepcopy
from random import randrange, random
from typing import Tuple, List

from chapter5.chromosome import Chromosome, T
from chapter5.genetic_algorithm import GeneticAlgorithm


class SimpleEquation(Chromosome):

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    @classmethod
    def random_instance(cls: SimpleEquation) -> SimpleEquation:
        return SimpleEquation(randrange(100), randrange(100))

    def fitness(self: SimpleEquation) -> float: # 6x - x^2 + 4y - y^2
        return 6 * self.x - self.x * self.x + 4 * self.y - self.y * self.y

    def crossover(self: SimpleEquation, other: SimpleEquation) -> Tuple[T, T]:
        child1: SimpleEquation = deepcopy(self)
        child2: SimpleEquation = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self: SimpleEquation) -> None:
        if random() < .5:
            if random() < .5:
                self.x += 1
            else:
                self.x -= 1
        else:
            if random() < .5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} Fitness: {self.fitness()}"


if __name__ == "__main__":
    initial_population: List[SimpleEquation] = [SimpleEquation.random_instance() for _ in range(20)]
    ga: GeneticAlgorithm = GeneticAlgorithm(initial_population=initial_population, threshold=13., max_generations=100,
                                            mutation_chance=.1, crossover_chance=.7)
    result = ga.run()
    print(result)
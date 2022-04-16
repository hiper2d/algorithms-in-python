from __future__ import annotations
from enum import Enum
from heapq import nlargest
from random import choices, random
from statistics import mean
from typing import TypeVar, Generic, List, Callable, Tuple

from chapter5.chromosome import Chromosome

C = TypeVar('C', bound=Chromosome)


class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(self, initial_population: List[C], threshold: float, max_generations: int = 100,
                 mutation_chance: float = .01, crossover_chance: float = .7,
                 selection_type: SelectionType = SelectionType.TOURNAMENT) -> None:
        self._population: List[C] = initial_population
        self._threshold: float = threshold
        self._max_generations: int = max_generations
        self._mutation_chance: float = mutation_chance
        self._crossover_chance: float = crossover_chance
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(initial_population[0]).fitness

    def __pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k=2))

    def __pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, self._fitness_key))

    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        while len(new_population) < len(self._population):
            if self._selection_type == GeneticAlgorithm.SelectionType.TOURNAMENT:
                parents = self.__pick_tournament(len(self._population) // 2)
            else:
                parents = self.__pick_roulette([x.fitness() for x in self._population])
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population

    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    def run(self) -> C:
        best: C = max(self._population, key=self._fitness_key)
        for gen in range(self._max_generations):
            if best.fitness() >= self._threshold:
                return best
            print(f"Generation {gen}, best {best.fitness()}, avg {mean(map(self._fitness_key, self._population))}")
            self._reproduce_and_replace()
            self._mutate()
            best_in_generation: C = max(self._population, key=self._fitness_key)
            if best_in_generation > best:
                best = best_in_generation
        return best


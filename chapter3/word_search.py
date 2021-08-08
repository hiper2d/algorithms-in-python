from random import choice
from string import ascii_uppercase
from typing import NamedTuple, List, Dict, Optional

from chapter3.csp import Constraint, CSP

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


Word_Location = List[GridLocation]


class WordSearchConstraint(Constraint[str, Word_Location]):
    def __init__(self, words: List[str]):
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, Word_Location]) -> bool:
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(all_locations) == len(set(all_locations))


def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(word: str, grid: Grid) -> List[Word_Location]:
    domain: List[Word_Location] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length + 1)
            rows: range = range(row, row + length + 1)
            # left to right
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                # diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            # top to bottom
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                # diagonal towards bottom left
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain


if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[Word_Location]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, Word_Location] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, Word_Location]] = csp.backtrack_search()
    if solution is None:
        print("There is no solution")
    else:
        for word, word_location in solution.items():
            if choice([True, False]):
                word_location.reverse()
            for index, letter in enumerate(word):
                (row, col) = (word_location[index].row, word_location[index].column)
                grid[row][col] = letter
        display_grid(grid)




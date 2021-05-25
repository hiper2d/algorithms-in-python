from random import choice
from string import ascii_uppercase
from typing import NamedTuple, List

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(row, row + length + 1)
            rows: range = range(col, col + length + 1)
            # left to right
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
            # diagonal towards bottom right
            # top to bottom
            # diagonal towards bottom left
    return domain
import random
from enum import Enum
from typing import NamedTuple, List


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    PATH = '*'
    START = 'S'
    GOAL = 'G'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self,
                 rows: int = 9,
                 columns: int = 9,
                 sparseness: float = .2,
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: MazeLocation = MazeLocation(9, 9),
                 ) -> None:
        self._rows = rows
        self._columns = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.START

    def _randomly_fill(self, rows: int, columns: int, sparseness: float) -> None:
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1.0) <= sparseness:
                    self._grid[r][c] = Cell.BLOCKED

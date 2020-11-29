import random
from enum import Enum
from typing import NamedTuple, List, Optional

from util.generic_search import dfs, Node, path_to_node


class Cell(str, Enum):
    EMPTY = '.'
    BLOCKED = 'X'
    PATH = '*'
    START = 'S'
    GOAL = 'G'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self,
                 rows: int = 10,
                 columns: int = 10,
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
        self._grid[goal.row][goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output

    def successors(self, current_location: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if current_location.row + 1 < self._rows \
                and self._grid[current_location.row+1][current_location.column] != Cell.BLOCKED:
            locations.append(MazeLocation(current_location.row+1, current_location.column))
        if current_location.row - 1 >= 0 \
                and self._grid[current_location.row - 1][current_location.column] != Cell.BLOCKED:
            locations.append(MazeLocation(current_location.row-1, current_location.column))
        if current_location.column + 1 < self._columns \
                and self._grid[current_location.row][current_location.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(current_location.row, current_location.column+1))
        if current_location.column - 1 >= 0 and \
                self._grid[current_location.row][current_location.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(current_location.row, current_location.column-1))
        return locations

    def goal_test(self, current_location: MazeLocation) -> bool:
        return self.goal == current_location

    def mark(self, p: List[MazeLocation]):
        for location in p:
            self._grid[location.row][location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, p: List[MazeLocation]):
        for location in p:
            self._grid[location.row][location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def get_cell(self, location: MazeLocation) -> Cell:
        return self._grid[location.row][location.column]

    def _randomly_fill(self, rows: int, columns: int, sparseness: float) -> None:
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1.0) <= sparseness:
                    self._grid[r][c] = Cell.BLOCKED


if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)
    solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print('There is not path')
    else:
        path: List[MazeLocation] = path_to_node(solution1)
        maze.mark(path)
        print(maze)
        maze.clear(path)


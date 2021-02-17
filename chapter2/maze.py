import random
from enum import Enum
from math import sqrt
from typing import NamedTuple, List, Optional, Callable

from util.generic_search import dfs, Node, path_to_node, bfs, astar


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


def euclidean_search(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(current: MazeLocation) -> float:
        x_dist = goal.row - current.row
        y_dist = goal.column - current.column
        return sqrt((x_dist * x_dist) + (y_dist * y_dist))
    return distance


def manhattan_search(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(current: MazeLocation) -> float:
        x_dist = abs(goal.row - current.row)
        y_dist = abs(goal.column - current.column)
        return x_dist + y_dist
    return distance


if __name__ == "__main__":
    print('u\004b')

    maze: Maze = Maze()
    print(maze)

    solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print('There is not path found with DFS')
    else:
        path1: List[MazeLocation] = path_to_node(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)

    solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
    if solution2 is None:
        print('There is not path found with BFS')
    else:
        path2: List[MazeLocation] = path_to_node(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)

    distance: Callable[[MazeLocation], float] = manhattan_search(maze.goal)
    solution3: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, distance)
    if solution3 is None:
        print('There is not path found with A*')
    else:
        path3: List[MazeLocation] = path_to_node(solution3)
        maze.mark(path3)
        print(maze)
        maze.clear(path3)


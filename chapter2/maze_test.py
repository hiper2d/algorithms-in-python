import unittest

from chapter2.maze import Maze, MazeLocation, Cell


class TestMazeMethods(unittest.TestCase):

    def setUp(self) -> None:
        self._maze = Maze()

    def test_successors(self):
        start: MazeLocation = self._maze.start
        start_successors: int = len(self._maze.successors(start))
        expected_successors = 0
        if self._maze.get_cell(MazeLocation(1, 0)) == Cell.EMPTY:
            expected_successors += 1
        if self._maze.get_cell(MazeLocation(0, 1)) == Cell.EMPTY:
            expected_successors += 1
        self.assertEqual(start_successors, expected_successors)


if __name__ == '__main__':
    unittest.main()

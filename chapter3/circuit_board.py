from typing import List, NamedTuple, Dict, Optional

from chapter3.csp import CSP, Constraint

Grid = List[List[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


class ChipLocation(NamedTuple):
    top_left: GridLocation
    bottom_right: GridLocation


class Chip(NamedTuple):
    id: int
    width: int
    height: int


class CircuitBoardLayoutConstraint(Constraint):
    def __init__(self, grid_size: int, chips: List[Chip]):
        super().__init__(chips)
        self.chips = chips
        self.grid_size = grid_size

    def satisfied(self, assignment: Dict[Chip, ChipLocation]) -> bool:
        chip_sum = 0
        temp_grid: Grid = generate_grid(self.grid_size)
        for (chip, chip_location) in assignment.items():
            add_chip_to_circuit_for_print(temp_grid, chip_location)
            chip_sum += chip.width * chip.height
        circuit_sum = sum(sum(r) for r in temp_grid)
        return circuit_sum == chip_sum


def generate_grid(size: int) -> Grid:
    return [[0 for col in range(size)] for row in range(size)]


def print_grid(grid: Grid):
    for row in grid:
        print(row)


def add_chip_to_circuit_for_print(grid: Grid, chip: ChipLocation):
    r1: int = chip.top_left.row
    r2: int = chip.bottom_right.row
    c1: int = chip.top_left.column
    c2: int = chip.bottom_right.column
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            grid[r][c] = 1


def place_chip_onto_circuit(grid_size: int, locations: List[ChipLocation],
                            chip_top_left_location: GridLocation, chip_bottom_right_location: GridLocation):
    if chip_bottom_right_location.row < grid_size and chip_bottom_right_location.column < grid_size:
        chip_location = ChipLocation(chip_top_left_location, chip_bottom_right_location)
        locations.append(chip_location)


def generate_domain(grid: Grid, chip: Chip) -> List[ChipLocation]:
    grid_size: int = len(grid)
    locations: List[ChipLocation] = []
    for row in range(grid_size):
        for col in range(grid_size):
            chip_top_left_location = GridLocation(row, col)
            # left to right
            chip_bottom_right_location = GridLocation(row + chip.width - 1, col + chip.height - 1)
            place_chip_onto_circuit(grid_size, locations, chip_top_left_location, chip_bottom_right_location)
            if chip.width != chip.height:
                # top to bottom
                chip_bottom_right_location = GridLocation(row + chip.height - 1, col + chip.width - 1)
                place_chip_onto_circuit(grid_size, locations, chip_top_left_location, chip_bottom_right_location)
    return locations


if __name__ == '__main__':
    grid_size = 10
    circuit: Grid = generate_grid(grid_size)
    chips: List[Chip] = [Chip(0, 3, 3), Chip(1, 3, 2), Chip(2, 9, 2), Chip(3, 1, 5), Chip(4, 9, 2), Chip(5, 10, 1)]
    chip_locations: Dict[Chip, List[ChipLocation]] = {}
    for chip in chips:
        chip_locations[chip] = generate_domain(circuit, chip)
    csp: CSP[Chip, ChipLocation] = CSP(chips, chip_locations)
    csp.add_constraint(CircuitBoardLayoutConstraint(grid_size, chips))
    solution: Optional[Dict[Chip, ChipLocation]] = csp.backtrack_search()
    if solution is None:
        print('There is not solution')
    else:
        for (chip, location) in solution.items():
            add_chip_to_circuit_for_print(circuit, location)
        print_grid(circuit)



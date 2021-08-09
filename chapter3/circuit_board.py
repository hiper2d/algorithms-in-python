from typing import List, NamedTuple, Dict, Optional

from chapter3.csp import CSP, Constraint, V, D

Grid = List[List[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


class ChipLocation(NamedTuple):
    top_left: GridLocation
    bottom_right: GridLocation


class Chip(NamedTuple):
    width: int
    height: int


class CircuitBoardLayoutConstraint(Constraint):
    def __init__(self, chips: List[Chip]):
        super().__init__(chips)
        self.chips = chips

    def satisfied(self, assignment: Dict[V, D]) -> bool:
        # todo: implement me
        ...


def generate_grid(size: int) -> Grid:
    return [[0 for col in range(size)] for row in range(size)]


def print_grid(grid: Grid):
    for row in grid:
        print(row)


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
    circuit: Grid = generate_grid(10)
    print_grid(circuit)
    chips: List[Chip] = [Chip(3, 3), Chip(3, 3), Chip(9, 2), Chip(1, 5)]
    chip_locations: Dict[Chip, List[ChipLocation]] = {}
    for chip in chips:
        chip_locations[chip] = generate_domain(circuit, chip)
    csp: CSP[Chip, ChipLocation] = CSP(chips, chip_locations)
    csp.add_constraint(CircuitBoardLayoutConstraint(chips))
    solution: Optional[Dict[Chip, ChipLocation]] = csp.backtrack_search()
    if solution is None:
        print('There is not solution')
    else:
        # todo: replace 0 with 1 for each chip in circuit
        print_grid(circuit)



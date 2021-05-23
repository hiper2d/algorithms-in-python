from typing import List, Dict, Optional

from chapter3.csp import CSP, Constraint, V, D


class QueensConstraint(Constraint[int, int]):

    def __init__(self, columns: List[int]):
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[V, D]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1c - q2c) == abs(q1r - q2r):
                        return False
        return True


if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtrack_search()
    if solution is None:
        print("No solutions")
    else:
        print(solution)

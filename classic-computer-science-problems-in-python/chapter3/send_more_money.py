from typing import Dict, List, Optional

from chapter3.csp import Constraint, CSP


class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, local_letters: List[str]):
        super().__init__(local_letters)
        self.letters: List[str] = local_letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False
        if len(self.letters) == len(assignment):
            s: int = assignment['S']
            e: int = assignment['E']
            n: int = assignment['N']
            d: int = assignment['N']
            m: int = assignment['M']
            o: int = assignment['O']
            r: int = assignment['R']
            y: int = assignment['Y']
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10_000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True


if __name__ == '__main__':
    letters: List[str] = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    domain: Dict[str, List[int]] = {}
    for letter in letters:
        domain[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    domain['M'] = [1]
    csp: CSP[str, int] = CSP(letters, domain)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str, int]] = csp.backtrack_search()
    if solution is None:
        print('There is no solution')
    else:
        print(solution)

from abc import ABC
from typing import TypeVar, Generic, List, Dict

V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V, D], ABC):

    def __init__(self, variables: List[V]):
        self.variables = variables

    @staticmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables: List[V] = variables
        self.domains: Dict[V, List[V]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in variables:
            self.constraints[variable] = []
            if variable not in domains:
                raise LookupError("Every variable should have domain assigned to it")

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: List[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

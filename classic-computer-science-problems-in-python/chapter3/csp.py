from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Dict, Optional

V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V, D], ABC):

    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):

    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
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

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtrack_search(self) -> Optional[Dict[V, D]]:
        return self.__backtrack_search({})

    def __backtrack_search(self, assignment: Dict[V, D]) -> Optional[Dict[V, D]]:
        if len(self.variables) == len(assignment):
            return assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first_variable: V = unassigned[0]
        for domain in self.domains[first_variable]:
            local_assignment = assignment.copy()
            local_assignment[first_variable] = domain
            if self.consistent(first_variable, local_assignment):
                result: Optional[Dict[V, D]] = self.__backtrack_search(local_assignment)
                if result is not None:
                    return result
        return None

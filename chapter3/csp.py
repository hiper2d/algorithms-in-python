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

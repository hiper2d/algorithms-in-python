# classic-computer-science-problems-in-python
Codding parts for Classic Computer Science Problems in Python book

Code examples for the book *Classic Computer Science Problems in Python* by David Kopec

![Classic Computer Science Problems in Python Cover](cover.jpg)

This project has a root which is a common for all chapters. For that reason, all imports start from `chapterX.file`. To run something from the console you need to set the environment variable with the root path:
```bash
export PYTHONPATH=/path-to-projects/classic-computer-science-problems-in-python
```
But I run everything including unit tests from the Intellij Idea where the project has a configured root.

# Python Tips

### Classes

Generics, static fields and methods, properties
```python
from typing import Generic, TypeVar, List

T = TypeVar('T')

class AwesomeClassWithGenerics(Generic[T]):
    static_field = 'ABC'
    # AwesomeClassWithGenerics.static_field and AwesomeClassWithGenerics().static_field are different
    # It's not possible to access static field via class instance variable
    
    def __init__(self, arg: T) -> None:
        self._property: T = arg 

    @staticmethod
    def some_static_method(arg: List[T]):
        ...

    @property
    def property(self) -> bool:
        return not self._property
```
Inheritance
```python
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Dict

V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V, D], ABC):

    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

class MapColoringConstraint(Constraint[str, str]):

    def __init__(self, place1: str, place2: str):
        # super() is sometimes used to call a method on the superclass,
        # but you can also use the name of the class itself, as in Constraint.__init__ ([place1, place2]).
        # This is especially helpful when dealing with multiple inheritance,
        # so that you know which superclass’s method you are calling.
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.place1 is not in assignment or self.place2 is not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]
```
Data Class and future module
```python
from __future__ import annotations
from dataclasses import dataclass

# A class marked with the @dataclass decorator saves some tedium
# by automatically creating an __init__() method that instantiates instance 
# variables for any variables declared with type annotations in the class’s body. 
# Dataclasses can also automatically create other special methods for a class. 
# Which special methods are automatically created is configurable via the decorator. 
# See the Python documentation on dataclasses for details (https://docs.python.org/3/library/dataclasses.html).
# In short, a dataclass is a way of saving ourselves some typing.

@dataclass
class Edge:
    u: int # the "from" vertex
    v: int # the "to" vertex

    # The method return the Edge class instance which is legal because the class 
    # is not yet defined. The __future__ import solves this problem.
    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"
```

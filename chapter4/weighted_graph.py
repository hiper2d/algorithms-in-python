from typing import TypeVar, Generic

from chapter4.graph import Graph

V = TypeVar('V')


class WeightedGraph(Generic[V], Graph[V]):
    pass

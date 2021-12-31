from math import exp
from typing import List


def dot_product(sx: List[float], ys: List[float]) -> float:
    return sum([x * y for x, y in zip(sx, ys)])


# the classic sigmoid activation function
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)
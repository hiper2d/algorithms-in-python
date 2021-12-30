from typing import List


def dot_product(sx: List[float], ys: List[float]) -> float:
    return sum([x * y for x, y in zip(sx, ys)])
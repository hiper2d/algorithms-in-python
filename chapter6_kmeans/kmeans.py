from statistics import pstdev, mean
from typing import Sequence, List


def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)
    if avg == 0:
        return [0] * len(original)
    return [(x - avg) / std for x in original]
from __future__ import annotations
from typing import List

MAX_NUM: int = 3


class MCState:
    def __init__(self, cannibals: int, missionaries: int, boat: bool):
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat = boat
        
    @property
    def is_legal(self) -> bool:
        if 0 < self.wm < self.wc:
            return False
        if 0 < self.em < self.ec:
            return False
        return True
        
    def goal_test(self):
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM
    
    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:
            if self.wm > 1:
                sucs.append(MCState(self.wc, self.wm - 2, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wc, self.wm - 1, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wc - 2, self.wm, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wc - 1, self.wm, not self.boat))
            if self.wc > 0 and self.wm > 0:
                sucs.append(MCState(self.wc - 1, self.wm - 1, not self.boat))
        else:
            if self.em > 1:
                sucs.append(MCState(self.ec, self.em + 2, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.ec, self.em + 1, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.ec + 2, self.em, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.ec + 1, self.em, not self.boat))
            if self.ec > 0 and self.em > 0:
                sucs.append(MCState(self.ec + 1, self.em + 1, not self.boat))
        return [x for x in sucs if x.is_legal]

    def __str__(self) -> str:
        return ("West bank has {} cannibals and {} missionaries.\n"
                "East bank has {} cannibals and {} missionaries.\n"
                "The boat is on the {} bank."
                ).format(self.wc, self.wm, self.ec, self.em, ("west" if self.boat else "east"))


if __name__ == "__main__":
    print(MCState(3, 3, True))


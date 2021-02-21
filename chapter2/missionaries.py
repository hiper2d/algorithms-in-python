from __future__ import annotations

from builtins import staticmethod
from typing import List, Optional

from util.generic_search import bfs, Node, path_to_node, dfs

MAX_NUM: int = 3


class MCState:
    def __init__(self, cannibals: int, missionaries: int, boat: bool):
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat = boat

    @staticmethod
    def display_solution(path: List[MCState]):
        if len(path) == 0:
            return
        old_state = path[0]
        for current_state in path[1:]:
            if current_state.boat:
                print('{} missionaries and {} cannibals were moved from the east bank to the west bank.\n'
                      .format(old_state.em - current_state.em, old_state.ec - current_state.ec))
            else:
                print('{} missionaries and {} cannibals were moved from the west bank to the east bank.\n'
                      .format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
            print(current_state)
            old_state = current_state

    @staticmethod
    def successors(state: MCState) -> List[MCState]:
        sucs: List[MCState] = []
        if state.boat:
            if state.wm > 1:
                sucs.append(MCState(state.wc, state.wm - 2, not state.boat))
            if state.wm > 0:
                sucs.append(MCState(state.wc, state.wm - 1, not state.boat))
            if state.wc > 1:
                sucs.append(MCState(state.wc - 2, state.wm, not state.boat))
            if state.wc > 0:
                sucs.append(MCState(state.wc - 1, state.wm, not state.boat))
            if state.wc > 0 and state.wm > 0:
                sucs.append(MCState(state.wc - 1, state.wm - 1, not state.boat))
        else:
            if state.em > 1:
                sucs.append(MCState(state.wc, state.wm + 2, not state.boat))
            if state.em > 0:
                sucs.append(MCState(state.wc, state.wm + 1, not state.boat))
            if state.ec > 1:
                sucs.append(MCState(state.wc + 2, state.wm, not state.boat))
            if state.ec > 0:
                sucs.append(MCState(state.wc + 1, state.wm, not state.boat))
            if state.ec > 0 and state.em > 0:
                sucs.append(MCState(state.wc + 1, state.wm + 1, not state.boat))
        return [x for x in sucs if x.is_legal]

    @staticmethod
    def goal_test(state: MCState) -> bool:
        return state.is_legal and state.em == MAX_NUM and state.ec == MAX_NUM

    @property
    def is_legal(self) -> bool:
        if 0 < self.wm < self.wc:
            return False
        if 0 < self.em < self.ec:
            return False
        return True

    def __str__(self) -> str:
        return ("West bank has {} cannibals and {} missionaries.\n"
                "East bank has {} cannibals and {} missionaries.\n"
                "The boat is on the {} bank.\n"
                ).format(self.wc, self.wm, self.ec, self.em, ("west" if self.boat else "east"))

    def __hash__(self) -> int:
        return hash((self.wc, self.ec, self.em, self.wm, self.boat))

    def __eq__(self, o: MCState) -> bool:
        return self.em == o.em \
               and self.ec == o.ec\
               and self.wm == o.wm \
               and self.wc == o.wc \
               and self.boat == o.boat


if __name__ == "__main__":
    original_state = MCState(MAX_NUM, MAX_NUM, True)
    solution: Optional[Node[MCState]] = bfs(original_state, MCState.goal_test, MCState.successors)
    if not solution:
        print('There is not solution for this problem')
    else:
        path: List[MCState] = path_to_node(solution)
        MCState.display_solution(path)
    


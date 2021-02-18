MAX_NUM: int = 3


class MCState:
    def __init__(self, cannibals: int, missionaries: int, boat: bool):
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat = boat

    def __str__(self) -> str:
        return ("West bank has {} cannibals and {} missionaries.\n"
                "East bank has {} cannibals and {} missionaries.\n"
                "The boat is on the {} bank."
                ).format(self.wc, self.wm, self.ec, self.em, ("west" if self.boat else "east"))


if __name__ == "__main__":
    print(MCState(3, 3, True))


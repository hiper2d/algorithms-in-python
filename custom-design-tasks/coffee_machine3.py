from abc import ABC
from enum import Enum


class CoffeeType(Enum):
    LATTE = 1
    CAPPUCCINO = 2
    ESPRESSO = 3


class CapSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3



class Coffee(ABC):
    def __init__(self, type: CoffeeType) -> None:
        self.type = type


class Latte(Coffee):
    def __init__(self, size: CapSize) -> None:
        super().__init__()


coffee_type_factory = {
    CoffeeType.LATTE: Latte()
}


class CoffeeMachine:
    def __init__(self):
        pass

    def make_coffee(self, type: CoffeeType) -> Coffee:
        return coffee_type_factory[type]



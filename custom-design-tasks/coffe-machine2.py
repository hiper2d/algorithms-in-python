from abc import ABC
from enum import Enum
from typing import TypeVar, Dict

T = TypeVar('T')


class Supply(ABC):
    ...


class Beans(Supply):
    def __repr__(self):
        return 'Beans'


class Water(Supply):
    ...


class Milk(Supply):
    ...


class BeverageType(Enum):
    COFFEE = 1
    TEA = 2
    HOT_CHOCOLATE = 3
    HOT_WATER = 4


class Beverage(ABC):
    def __init__(self, type: BeverageType):
        self.type = type

    @property
    def recipy(self) -> Dict[Supply, int]:
        ...


class Coffee(Beverage):
    def __init__(self):
        super().__init__(BeverageType.COFFEE)

    @property
    def recipy(self) -> Dict[Supply, int]:
        return {Beans: 1, Water: 1, Milk: 1}


class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups


if __name__ == '__main__':
    machine = CoffeeMachine(400, 540, 120, 9)
    coffee = Coffee()
    r: Dict[Supply, int] = coffee.recipy
    print(r)

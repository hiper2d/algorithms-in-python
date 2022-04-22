from enum import Enum
from typing import Optional


class RoastType(Enum):
    LIGHT = 1
    DARK = 2


class CoffeeType(Enum):
    ESPRESSO = 1
    LATTE = 2
    CAPPUCCINO = 3
    NITRO = 4
    RAPH = 5
    BULLET_PROOFY = 6


class CoffeeCupSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


watter_function = {
    CoffeeCupSize.SMALL: 10,
    CoffeeCupSize.MEDIUM: 15,
    CoffeeCupSize.LARGE: 20
}


class Drink:
    def __init__(self, roast: RoastType):
        self.__roast = roast

    @property
    def get_type(self):
        pass


class Cappuccino(Drink):
    def __init__(self, roast: RoastType):
        super().__init__(roast)

    @property
    def get_type(self):
        return CoffeeType.CAPPUCCINO


class CoffeeCup:
    def __init__(self, size: CoffeeCupSize):
        self.size: CoffeeCupSize = size
        self.coffee: Optional[Drink] = None


class CoffeeMachine:
    def __init__(self):
        self.watter_level = 0
        self.cups = {
            CoffeeCupSize.SMALL: 0,
            CoffeeCupSize.MEDIUM: 0,
            CoffeeCupSize.LARGE: 0
        }

    def make_coffee(self, coffee_type: CoffeeType, roast_type, cup_size: CoffeeCupSize) -> Optional[CoffeeCup]:
        if self.watter_level < 20:
            print("Warning: Please fill the watter")
            return

        if self._low_on_cups():
            print("Warning: Please fill the cups")
            return

        drink: Drink = self._prepare_drink(roast_type, coffee_type)
        cup_with_coffee: CoffeeCup = self._pour_into_cup(drink, cup_size)
        print(f"Drink is ready {cup_with_coffee}")

    def fill_watter(self):
        self.watter_level = 100

    def fill_cups(self):
        self.cups[CoffeeCupSize.SMALL] = 10
        self.cups[CoffeeCupSize.MEDIUM] = 10
        self.cups[CoffeeCupSize.LARGE] = 10

    def _low_on_cups(self) -> bool:
        return True if self.cups[CoffeeCupSize.SMALL] < 1 \
                       or self.cups[CoffeeCupSize.MEDIUM] < 1 \
                       or self.cups[CoffeeCupSize.LARGE] < 1 \
            else False

    def _prepare_drink(self, roast_type: RoastType, coffee_type: CoffeeType, cup_size: CoffeeCupSize) -> Drink:
        print(f"Preparing {coffee_type}")
        self.watter_level -= watter_function[cup_size]
        return Cappuccino(roast_type) if coffee_type == CoffeeType.CAPPUCCINO \
            else Cappuccino(roast_type)

    def _pour_into_cup(self, drink: Drink, cup_size: CoffeeCupSize) -> CoffeeCup:
        print(f"Pouring {drink} into cup")
        self.cups[cup_size] -= 1
        cup = CoffeeCup(cup_size)
        cup.coffee = drink
        return cup

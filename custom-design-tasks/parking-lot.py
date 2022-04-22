from abc import ABC, abstractmethod
from enum import Enum


class LotType(Enum):
    COMPACT, REGULAR, LARGE = 1, 2, 3


class Lot(ABC):
    def __init__(self, id: int):
        self.id = id
        self.occupied = False
        # self.reservation_start
        # self.reservation_end

    @abstractmethod
    @property
    def get_type(self) -> LotType:
        ...


class CompactLot(Lot):
    @property
    def get_type(self) -> LotType:
        return LotType.COMPACT


class RegularLot(Lot):
    @property
    def get_type(self) -> LotType:
        return LotType.REGULAR


class LargeLot(Lot):
    @property
    def get_type(self) -> LotType:
        return LotType.LARGE


class Customer:
    def __init__(self):
        # self.id = rand_uuid()
        pass


class ParkingLot:
    def __init__(self, compact_lots: int, regular_lots: int, large_lots: int):
        pass

    def reserve(self, client_id: Customer, lot_type: LotType):
        ...

from typing import TypeVar, Generic, OrderedDict

K = TypeVar('K')
V = TypeVar('V')


class LruCacheOrderedDict(OrderedDict[K, V]):
    def __init__(self, max_capacity: int):
        super().__init__()
        self.capacity = max_capacity

    def get(self, key: K) -> V:
        if key not in self.lookup:
            raise KeyError('No such key')
        self.lookup.move_to_end(key)
        return self.lookup[key]

    def set(self, key: K, val: V) -> None:
        if key in self.lookup:
            self.lookup.move_to_end(key)
        else:
            if self.capacity < self.max_capacity:
                self.capacity += 1
            else:
                self.lookup.popitem(key)
        self.lookup[key] = val

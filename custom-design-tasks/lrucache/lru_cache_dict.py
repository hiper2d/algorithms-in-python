from typing import Generic, TypeVar, Dict

K = TypeVar('K')
V = TypeVar('V')


class LruCacheDict(Generic[K, V]):
    def __init__(self, max_capacity: int):
        self.capacity = 0
        self.max_capacity = max_capacity
        self.lookup: Dict[K, V] = dict[K, V]()

    def get(self, key: K) -> V:
        if key not in self.lookup:
            raise KeyError("No such key")
        val = self.lookup.pop(key)
        self.lookup[key] = val
        return val

    def __getitem__(self, item):
        return self.get(item)

    def set(self, key: K, value: V) -> None:
        if key in self.lookup:
            del self.lookup[key]
        else:
            if self.capacity < self.max_capacity:
                self.capacity += 1
            else:
                del self.lookup[next(iter(self.lookup))]
        self.lookup[key] = value

    def __setitem__(self, key, value):
        self.set(key, value)

# 1Z97YY619026207830
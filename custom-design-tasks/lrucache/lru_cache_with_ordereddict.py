from typing import TypeVar, Generic, OrderedDict, Optional

K = TypeVar('K')
V = TypeVar('V')


class LruCacheWithOrderedDict(Generic[K, V]):
    def __init__(self, capacity: int):
        self.max_capacity: int = capacity
        self.capacity: int = 0
        self.storage: OrderedDict[K, V] = OrderedDict[K, V]()

    def put(self, key: K, value: V) -> None:
        if value in self.storage:
            self.storage[key] = value
            self.storage.move_to_end(key)
        else:
            if self.capacity == self.max_capacity:
                self.storage.popitem(last=False)
            else:
                self.capacity += 1
            self.storage[key] = value

    def get(self, key: K) -> Optional[V]:
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        else:
            return None

    def __getitem__(self, key: K):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

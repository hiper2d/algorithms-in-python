from collections import deque
from typing import Generic, TypeVar, Dict, Deque, Optional

K = TypeVar('K')
V = TypeVar('V')


class LruCache(Generic[K, V]):
    def __init__(self, max_capacity: int = 10):
        self.max_capacity: int = max_capacity
        self.capacity: int = 0
        self.lookup: Dict[K, V] = {}
        self.fifo: Deque[K] = deque()

    def get(self, key: K) -> Optional[V]:
        if key in self.lookup:
            return self.lookup[key]
        else:
            return None

    def __getitem__(self, key: K) -> Optional[V]:
        return self.get(key)

    def put(self, key: K, value: V):
        if key not in self.lookup:
            if self.capacity < self.max_capacity:
                self.capacity += 1
            else:
                self.fifo.popleft()
            self.fifo.append(key)
        self.lookup[key] = value

    def __setitem__(self, key: K, value: V):
        self.put(key, value)
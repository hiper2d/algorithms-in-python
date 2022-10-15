from collections import deque
from typing import Generic, TypeVar, Dict, Deque, Optional

K = TypeVar('K')
V = TypeVar('V')


class LruCache(Generic[K, V]):
    def __init__(self, max_capacity: int):
        self.lookup: Dict[K, V] = {}
        self.queue = deque()
        self.capacity = 0
        self.max_capacity = max_capacity

    def put(self, key: K, value: V) -> None:
        if key not in self.lookup:
            self.lookup[key] = value
            self.queue.append(key)
            self.capacity += 1
            if self.capacity > self.max_capacity:
                key_for_removal = self.queue.popleft()
                del self.lookup[key_for_removal]
                self.capacity -= 1
        else:
            self.lookup[key] = value
            self._move_key_to_queue_end(key)

    def __setitem__(self, key: K, value: V) -> None:
        self.put(key, value)

    def get(self, key: K) -> Optional[V]:
        if key in self.lookup:
            self._move_key_to_queue_end(key)
            return self.lookup[key]
        else:
            return None

    def __getitem__(self, key: K) -> Optional[V]:
        return self.get(key)

    def _move_key_to_queue_end(self, key: K):
        self.queue.remove(key)
        self.queue.append(key)

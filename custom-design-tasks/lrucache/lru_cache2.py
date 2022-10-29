from typing import Generic, TypeVar, OrderedDict, Tuple

K = TypeVar('K')
V = TypeVar('V')


class NoSuchKeyException(Exception):
    ...


class LruCache2(Generic[K, V]):
    def __init__(self, max_size: int):
        self.lookup: OrderedDict[K, V] = OrderedDict[K, V]()
        self.max_size = max_size
        self._size = 0

    def put(self, key: K, val: V) -> None:
        if key in self.lookup:
            self.lookup[key] = val
            self.lookup.move_to_end(key)
        else:
            if self._size == self.max_size:
                self.lookup.popitem(last=False)
                self.lookup[key] = val
            else:
                self.lookup[key] = val
                self._size += 1

    def get(self, key: K) -> V:
        if key in self.lookup:
            self.lookup.move_to_end(key)
            return self.lookup[key]
        else:
            raise NoSuchKeyException()

    def peak(self) -> Tuple[K, V]:
        return next(reversed(self.lookup))

    def peakleft(self) -> Tuple[K, V]:
        return next(iter(self.lookup))

    def __getitem__(self, key: K) -> V:
        return self.get(key)

    def __setitem__(self, key: K, value: V) -> None:
        self.put(key, value)


class LruCache2Test:

    @staticmethod
    def test_lest_recent_used_item_evicted():
        c = LruCache2(max_size=2)
        c[1] = "one"
        c[2] = "two"
        c[3] = "tree"
        print(f"c[2] is {c[2]} when expected two")
        try:
            c[1]  # expect Error
        except NoSuchKeyException as e:
            print(f"c[1] expects NoSuchKeyException, got {type(e)}")

    @staticmethod
    def test_accessed_items_are_moved_to_tail():
        c = LruCache2(max_size=3)
        c[1] = 1
        c[2] = 2
        c[3] = 3
        print(f"First item should be 1 while it's {c.peakleft()}")
        print(f"Last item should be 3 while it's {c.peak()}")
        c[2]
        print(f"After accessing c[2] it should be the last item, while it's {c.peak()}")
        c[1] = 1
        print(f"After reassigning c[1] it should be the last item, while it's {c.peak()}")
        print(f"After reassigning c[1] c[3] should be the first item, while it's {c.peakleft()}")

    @staticmethod
    def run_test():
        LruCache2Test.test_lest_recent_used_item_evicted()
        LruCache2Test.test_accessed_items_are_moved_to_tail()


if __name__ == "__main__":
    LruCache2Test.run_test()
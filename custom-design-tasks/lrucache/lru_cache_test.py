import unittest

from lrucache.lru_cache import LruCache
from lrucache.lru_cache_with_ordereddict import LruCacheWithOrderedDict


class LruCacheTest(unittest.TestCase):

    def test_removal_when_exceeds_capacity(self):
        cache = LruCache(3)
        cache[1] = "one"
        cache.put(2, "two")
        cache.put(3, "three")
        self.assertEqual("two", cache.get(2))

    def test_ordereddict_add_and_get_values(self):
        cache = LruCacheWithOrderedDict(3)
        cache[1] = "one"
        cache.put(2, "two")
        cache.put(3, "three")
        self.assertEqual("two", cache.get(2))

    def test_oredereddict_removal_when_exceeds_capacity(self):
        cache = LruCacheWithOrderedDict(1)
        cache[1] = "one"
        self.assertEqual("one", cache[1])
        cache[2] = "two"
        self.assertIsNone(cache[1])
        self.assertEqual("two", cache[2])


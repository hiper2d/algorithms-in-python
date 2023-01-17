import unittest

from lrucache.lru_cache_dict import LruCacheDict
from lrucache.lru_cache_ordereddict import LruCacheOrderedDict


class LruCacheTest(unittest.TestCase):

    def test_normal_insertion(self):
        cache = LruCacheOrderedDict(2)
        cache[1] = 1
        cache[2] = 2
        cache[3] = 3  # cache should contain [2, 3]
        self.assertEqual(2, cache[2])  # cache should contain [3, 2]
        with self.assertRaises(KeyError):
            cache[1]
        cache[4] = 4  # cache should contain [2, 4]
        with self.assertRaises(KeyError):
            cache[3]


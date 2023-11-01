from unittest import TestCase

from LRUCache import LRUCache
import time


class LRUCacheTest(TestCase):
    def test_default_input(self):
        cache = LRUCache(2)
        expiry_time = 60  # 60 seconds
        cache.put(1, 1, expiry_time)  # cache is {1=1}
        cache.put(2, 2, expiry_time)  # cache is {1=1, 2=2}
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3, expiry_time)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4, expiry_time)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_put_items_only(self):
        cache = LRUCache(3)
        expiry_time = 60  # 60 seconds
        cache.put(1, 1, expiry_time)
        cache.put(2, 2, expiry_time)
        cache.put(3, 3, expiry_time)
        cache.put(4, 4, expiry_time)
        cache.put(5, 5, expiry_time)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), -1)
        cache.put(6, 6, expiry_time)
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(6), 6)

    def test_single_item_capacity(self):
        cache = LRUCache(1)
        expiry_time = 60  # 60 seconds

        cache.put(2, 1, expiry_time)

        self.assertEqual(cache.get(1), -1)

    def test_item_replacing(self):
        cache = LRUCache(2)
        expiry_time = 60  # 60 seconds

        cache.put(2, 1, expiry_time)
        cache.put(2, 2, expiry_time)

        self.assertEqual(cache.get(2), 2)

    def test_zero_values(self):
        cache = LRUCache(2)
        expiry_time = 60  # 60 seconds

        cache.put(1, 0, expiry_time)
        cache.put(2, 2, expiry_time)

        self.assertEqual(cache.get(1), 0)

        cache.put(3, 3, expiry_time)

        self.assertEqual(cache.get(2), -1)

        cache.put(4, 4, expiry_time)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_long_list_of_values(self):
        cache = LRUCache(10)
        expiry_time = 60  # 60 seconds

        for (key, value) in [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10]]:
            cache.put(key, value, expiry_time)
        self.assertEqual(cache.get(13), -1)

        cache.put(2, 19, expiry_time)

        self.assertEqual(cache.get(2), 19)
        self.assertEqual(cache.get(3), 17)

        cache.put(5, 25, expiry_time)

        self.assertEqual(cache.get(8), -1)

        cache.put(9, 12, expiry_time)

        self.assertEqual(cache.get(7), -1)
        self.assertEqual(cache.get(5), 25)
        self.assertEqual(cache.get(8), -1)
        self.assertEqual(cache.get(9), 12)

        cache.put(4, 30, expiry_time)
        cache.put(9, 3, expiry_time)

        self.assertEqual(cache.get(9), 3)
        self.assertEqual(cache.get(10), 5)
        self.assertEqual(cache.get(10), 5)

        cache.put(6, 14, expiry_time)
        cache.put(3, 1, expiry_time)

        self.assertEqual(cache.get(3), 1)

        cache.put(10, 11, expiry_time)

        self.assertEqual(cache.get(8), -1)

        cache.put(2, 14, expiry_time)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(5), 25)
        self.assertEqual(cache.get(4), 30)


import time
from collections import OrderedDict
from typing import Dict, Optional
from Node import Node
from LinkedList import LinkedList

class LRUCache:

    capacity: int
    cache_map: Dict[int, Node]
    history: LinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.history = LinkedList()


    def get(self, key: int) -> int:
        # Retrieve value by its key or -1 otherwise
        if key not in self.cache_map:
            return -1

        value_node: Node = self.cache_map[key]

        if self.history.head != value_node:
            # make item the most recently used
            self.history.unlink(value_node)
            self.history.add_to_head(value_node)

        return value_node.value

    def put(self, key: int, value: int, expiry_time: int) -> None:
        """
        Add a new key-value pair to the cache.
        If key exists, replace its value by a new one.
        If capacity is reached, evict the LRU item and insert a new pair
        """
        value_node: Node = Node(key, value, time.time() + expiry_time) # in seconds

        if key in self.cache_map:
            self.remove_item(self.cache_map[key])

        if len(self.cache_map) >= self.capacity:
            # no space left, needs to evict the least recently used item
            self.evict_least_recent_item()

        self.history.add_to_head(value_node)
        self.cache_map[key] = value_node

    def remove_expired_items(self) -> None:
        # Remove expired items from the cache
        current_time = time.time()

        for node in list(self.cache_map.values()):
            if node.expiry_time < current_time:
                self.remove_item(node)

    def evict_least_recent_item(self) -> None:
        lru_item: Node = self.history.tail

        if lru_item is None:
            return

        self.remove_item(lru_item)

    def remove_item(self, item: Node) -> None:
        """
        Remove item represented by node from the map and the list
        """
        self.history.unlink(item)

        del self.cache_map[item.key]
        del item

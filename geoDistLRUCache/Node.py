from typing import Dict, Optional


class Node:
    """
    Linked List Node. Contains key-value pair and links to neighbor elements.
    """

    def __init__(self, capacity: int, expiration: int, key: int, value: int, prev=None, next=None):
        self.capacity = capacity
        self.expiration = expiration
        self.key: int = key
        self.value: int = value
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next





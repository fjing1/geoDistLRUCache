from typing import Dict, Optional


class Node:
    """
    Linked List Node. Contains key-value pair and links to neighbor elements.
    """

    def __init__(self, key: int, value: int, expiration: int, prev=None, next=None):
        self.expiration = expiration
        self.key: int = key
        self.value: int = value
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next





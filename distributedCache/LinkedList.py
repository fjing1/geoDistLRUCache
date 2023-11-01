from Node import Node


class LinkedList:
    """
    Linked List. Represents usage history of cache items
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, item: Node) -> None:
        """
        Add node to the very top of the list
        """
        if self.head is not None:
            item.next = self.head
            self.head.prev = item

        if self.tail is None:
            self.tail = item

        self.head = item

    def unlink(self, item: Node) -> None:
        """
        Remove references to the node from other nodes on the list
        """
        if item is None:
            return

        prev_item: Node = item.prev
        next_item: Node = item.next

        # unlink the item node:
        # link prev and next items
        # removing referenced to the current item node
        if prev_item is not None:
            prev_item.next = next_item

        if next_item is not None:
            next_item.prev = prev_item

        if self.head == item:
            # item was the first element in the list
            self.head = next_item
        if self.tail == item:
            # item was the last element in the list
            self.tail = prev_item

        # make sure that the item itself doesn't have references to other nodes
        item.prev = None
        item.next = None

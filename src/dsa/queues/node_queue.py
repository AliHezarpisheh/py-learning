"""Module containing Node Based Queue."""

from typing import Any


class Node:
    """Doubly Linked List Node."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous = None
        self.next = None


class NodeBasedQueue:
    """Represent a node-based queue data structure."""

    def __init__(self):
        """Initialize a node-based queue data structure."""
        self.head = None  # First element in the list
        self.tail = None  # Last element in the list
        self.size = 0

    def enqueue(self, data: Any) -> None:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : Any
            The data to enqueue.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self) -> Any:
        """
        Remove and return the first element in the list.

        Returns
        -------
        Any
            The data of the removed element.
        """
        if self.size == 1:
            data = self.head
            self.head = self.tail = None
            self.size -= 1
            return data
        elif self.size > 1:
            data = self.head.data
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
            return data

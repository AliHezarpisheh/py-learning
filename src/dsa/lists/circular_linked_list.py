from typing import Generator, Any


class Node:
    def __init__(
        self,
        data: Any | None = None,
        previous: "Node" | None = None,
        next: "Node" | None = None,
    ) -> None:
        self.data = data
        self.next = next
        self.previous = previous


class SinglyCircularLinkedList:
    """Represent a singly circular linked list data structure."""

    def __init__(self) -> None:
        """Initialize a singly circular linked list data structure."""
        self.tail = None  # First element in the list
        self.head = None  # Last element in the list
        self.count = 0

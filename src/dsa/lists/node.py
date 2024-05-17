from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        """Doubly Linked List Node."""
        self.data = data
        self.next = None
        self.previous = None

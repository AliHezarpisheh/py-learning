from typing import Any


class Node:
    """Class representing a Node in a Doubly Linked List."""

    def __init__(self, data: Any) -> None:
        """Instantiate Node."""
        self.data = data
        self.next = None
        self.previous = None

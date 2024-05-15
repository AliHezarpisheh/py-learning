from typing import Any


class Node:
    """Node class."""

    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with the given data.

        Parameters
        ----------
        data : Any
            The data to be stored in the node.
        """
        self.data = data
        self.next = None


class NodeStack:
    """Implementation of a stack using linked list nodes."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self.top = None
        self.size = 0

    def push(self, data: Any) -> None:
        """
        Push an item onto the top of the stack.

        Parameters
        ----------
        data : Any
            The data to be pushed onto the stack.
        """
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.size += 1

    def pop(self) -> Any | None:
        """
        Remove and returns the item at the top of the stack.

        Returns
        -------
        Any or None
            The data of the item removed from the top of the stack, or None if the stack
            is empty.
        """
        if not self.top:
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self) -> Any:
        """
        Return the data of the item at the top of the stack without removing it.

        Returns
        -------
        Any or None
            The data of the item at the top of the stack, or None if the stack is empty.
        """
        if self.top:
            return self.top.data
        else:
            return None

    def __len__(self) -> int:
        """Return the siz of the stack."""
        return self.size

    def __bool__(self) -> bool:
        return self.size > 0

"""Module containing Array Based Stack."""

from typing import Any


class ListStack:
    """Implementation of a stack using a Python list."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self.items = []

    def push(self, data: Any) -> None:
        """
        Push an item onto the top of the stack.

        Parameters
        ----------
        data : Any
            The data to be pushed onto the stack.
        """
        self.items.append(data)

    def pop(self) -> Any | None:
        """
        Remove and returns the item at the top of the stack.

        Returns
        -------
        Any or None
            The data of the item removed from the top of the stack, or None if the stack is empty.
        """
        if not self.items:
            return None

        return self.items.pop()

    def peek(self) -> Any:
        """
        Return the data of the item at the top of the stack without removing it.

        Returns
        -------
        Any or None
            The data of the item at the top of the stack, or None if the stack is empty.
        """
        if not self.items:
            return None
        return self.items[-1]

    def __len__(self) -> int:
        """Return the siz of the stack."""
        return len(self.items)

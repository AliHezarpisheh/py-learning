"""Module containing Doubly Linked List."""

from __future__ import annotations

from typing import Any, Generator


class Node:
    def __init__(
        self,
        data: Any = None,
        previous: Node | None = None,
        next: Node | None = None,
    ) -> None:
        """Doubly Linked List Node."""
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList:
    """Represent a doubly linked list data structure."""

    def __init__(self) -> None:
        """Initialize a doubly linked list data structure."""
        self.head = None  # First element in the list
        self.tail = None  # Last element in the list
        self.count = 0

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Return an iterator over the elements of the list.

        Yields
        ------
        Any
            The data of each node in the list.
        """
        current = self.head
        while current:
            data = current.data
            yield data
            current = current.next

    def __getitem__(self, index: int) -> Any:
        """
        Return the data at the specified index in the list.

        Parameters
        ----------
        index : int
            The index of the element to retrieve.

        Returns
        -------
        Any
            The data at the specified index.

        Raises
        ------
        IndexError
            If the index is out of range.
        """
        assert isinstance(index, int), f"Index should be `int`, got `{type(index)}`"

        if index > self.count - 1:
            raise IndexError("Index out of range.")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index: int, value: Any) -> Any:
        """
        Set the data at the specified index in the list.

        Parameters
        ----------
        index : int
            The index of the element to set.
        value : Any
            The new value to set at the specified index.

        Raises
        ------
        IndexError
            If the index is out of range.
        """
        assert isinstance(index, int), f"Index should be `int`, got `{type(index)}`"

        if index > self.count - 1:
            raise IndexError("Index out of range.")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def __contains__(self, data: Any) -> bool:
        """
        Search for the specified data in the list.

        Parameters
        ----------
        data : Any
            The data to search for.

        Returns
        -------
        bool
            True if the data is found, False otherwise.
        """
        for node_data in self:
            if node_data == data:
                return True
        return False

    def append(self, data: Any) -> None:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : Any
            The data to append to the list.
        """
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def delete(self, data: Any) -> None:
        """
        Delete the first occurrence of the specified data from the list.

        Parameters
        ----------
        data : Any
            The data to delete from the list.
        """
        current = self.head
        while current:
            if current.data == data:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                self.count -= 1
                return True
            current = current.next
        return False

    def reverse_iter(self) -> Generator[Any, None, None]:
        """Iterate in the reverse order of the list."""
        current = self.tail
        while current:
            data = current.data
            yield data
            current = current.previous

    def clear(self) -> None:
        """Clear the list."""
        self.head = self.tail = None
        self.count = 0

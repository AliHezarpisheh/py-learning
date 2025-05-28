"""Module containing Circular Linked Lists."""

from __future__ import annotations

from typing import Generator, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """Node class for singly linked lists, pointing to the next node."""

    def __init__(self, data: T) -> None:
        """Initialize a `Node` instance."""
        self.data = data
        self.next = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"Node <data={self.data} next={self.next}>"

    def __repr__(self) -> str:
        """Return a string representation of the node for debugging purposes."""
        return f"Node(data={self.data})"


class CircularSinglyLinkedList(Generic[T]):
    """Circular singly linked list with support of multiple common operations."""

    def __init__(self) -> None:
        """Initiliaze a `CircularSinglyLinkedList` instnace."""
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data: T) -> bool:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : T
            The data to store in the new node.

        Returns
        -------
        bool
            `True` if the node was successfully appended, otherwise `False`.
        """
        new_node = Node(data=data)
        if self.tail:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            self.head = self.tail = new_node
            self.head.next = new_node
            self.tail.next = new_node
        self.count += 1
        return True

    def delete(self, data: T) -> bool:
        """
        Delete the first node containing the specified data.

        Parameters
        ----------
        data : T
            The data to search for and remove.

        Returns
        -------
        bool
            `True` if the node was successfully deleted, otherwise `False`.
        """
        previous = self.tail
        current = self.head
        if current is None:
            return False

        while True:
            if current.data == data:
                if self.count == 1:
                    return self.clear()

                previous.next = current.next
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = previous
                self.count -= 1
                return True
            if current == self.tail:
                return False
            previous = current
            current = current.next

    def clear(self) -> bool:
        """
        Remove all nodes from the list.

        Returns
        -------
        bool
            `True` if the list was successfully cleared.
        """
        self.head = self.tail = None
        self.count = 0
        return True

    def __len__(self) -> int:
        """
        Return the number of nodes in the list.

        Returns
        -------
        int
            The number of nodes in the list.
        """
        return self.count

    def __getitem__(self, index: int) -> T:
        """
        Get the data of the node at the specified index.

        Parameters
        ----------
        index : int
            The index of the node to retrieve.

        Returns
        -------
        T
            The data of the node at the given index.

        Raises
        ------
        TypeError
            If the index is not an integer.
        IndexError
            If the index is out of range.
        """
        if not isinstance(index, int):
            raise TypeError("index should be int")
        if index >= self.count:
            raise IndexError("index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index: int, data: T) -> None:
        """
        Set the data of the node at the specified index.

        Parameters
        ----------
        index : int
            The index of the node to modify.
        data : T
            The new data to store in the node.

        Raises
        ------
        TypeError
            If the index is not an integer.
        IndexError
            If the index is out of range.
        """
        if not isinstance(index, int):
            raise TypeError("index should be int")
        if index >= self.count:
            raise IndexError("index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __iter__(self) -> Generator[T, None, None]:
        """
        Iterate over the data in the list.

        Yields
        ------
        T
            The data from each node in the list.

        Notes
        -----
        Iteration will stop when the loop returns to the head node, ensuring
        the circular nature of the list.
        """
        current = self.head
        while True:
            data = current.data
            yield data
            current = current.next
            if current == self.head:
                break

    def __contains__(self, data: T) -> bool:
        """
        Check if a node with the specified data exists in the list.

        Parameters
        ----------
        data : T
            The data to search for.

        Returns
        -------
        bool
            `True` if the data is found in the list, otherwise `False`.
        """
        for node_data in self:
            if node_data == data:
                return True
        return False

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        return " -> ".join(str(data) for data in self)

    def __repr__(self) -> str:
        """Return a string representation of the linked list for debugging purposes."""
        return " -> ".join(str(data) for data in self)


class Node(Generic[T]):  # noqa: F811
    """Node class for doubly linked lists, pointing to next and previous nodes."""

    def __init__(self, data: T) -> None:
        """Initialize a `Node` instance."""
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"Node <data={self.data} next={self.next}>"

    def __repr__(self) -> str:
        """Return a string representation of the node for debugging purposes."""
        return f"Node(data={self.data})"


class CircularDoublyLinkedList(Generic[T]):
    """Circular doubly linked list with support of multiple common operations."""

    def __init__(self) -> None:
        """Initialize a `CircularDoublyLinkedList` instance."""
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data: T) -> bool:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : T
            The data to store in the new node.

        Returns
        -------
        bool
            `True` if the node was successfully appended, otherwise `False`.
        """
        new_node = Node(data=data)
        if self.tail:
            new_node.previous = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.previous = new_node
        else:
            self.head = self.tail = new_node
            self.head.previous = self.head.next = new_node
            self.tail.previous = self.tail.next = new_node
        self.count += 1
        return True

    def delete(self, data: T) -> bool:
        """
        Delete the first node containing the specified data.

        Parameters
        ----------
        data : T
            The data to search for and remove.

        Returns
        -------
        bool
            `True` if the node was successfully deleted, otherwise `False`.
        """
        current = self.head

        if current is None:
            return False

        while current:
            if current.data == data:
                if self.count == 1:
                    return self.clear()

                current.previous.next = current.next
                current.next.previous = current.previous
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = current.previous
                self.count -= 1
                return True

            if current == self.tail:
                break

            current = current.next
        return False

    def clear(self) -> bool:
        """
        Remove all nodes from the list.

        Returns
        -------
        bool
            `True` if the list was successfully cleared.
        """
        self.head = self.tail = None
        self.count = 0
        return True

    def __len__(self) -> int:
        """
        Return the number of nodes in the list.

        Returns
        -------
        int
            The number of nodes in the list.
        """
        return self.count

    def __getitem__(self, index: int) -> T:
        """
        Get the data of the node at the specified index.

        Parameters
        ----------
        index : int
            The index of the node to retrieve.

        Returns
        -------
        T
            The data of the node at the given index.

        Raises
        ------
        TypeError
            If the index is not an integer.
        IndexError
            If the index is out of range.
        """
        if not isinstance(index, int):
            raise TypeError("index should be int")
        if index >= self.count:
            raise IndexError("index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index: int, data: T) -> None:
        """
        Set the data of the node at the specified index.

        Parameters
        ----------
        index : int
            The index of the node to modify.
        data : T
            The new data to store in the node.

        Raises
        ------
        TypeError
            If the index is not an integer.
        IndexError
            If the index is out of range.
        """
        if not isinstance(index, int):
            raise TypeError("index should be int")
        if index >= self.count:
            raise IndexError("index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __iter__(self) -> Generator[T, None, None]:
        """
        Iterate over the data in the list.

        Yields
        ------
        T
            The data from each node in the list.

        Notes
        -----
        Iteration will stop when the loop returns to the head node, ensuring
        the circular nature of the list.
        """
        current = self.head
        while True:
            data = current.data
            yield data
            current = current.next
            if current == self.head:
                break

    def __contains__(self, data: T) -> bool:
        """
        Check if a node with the specified data exists in the list.

        Parameters
        ----------
        data : T
            The data to search for.

        Returns
        -------
        bool
            `True` if the data is found in the list, otherwise `False`.
        """
        for node_data in self:
            if node_data == data:
                return True
        return False

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        return " <-> ".join(str(data) for data in self)

    def __repr__(self) -> str:
        """Return a string representation of the linked list for debugging purposes."""
        return " <-> ".join(str(data) for data in self)

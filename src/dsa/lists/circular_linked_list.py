from typing import Generator, Any


class Node:
    def __init__(
        self,
        data: Any | None = None,
        next: "Node" | None = None,
    ) -> None:
        self.data = data
        self.next = next


class SinglyCircularLinkedList:
    """Represent a singly circular linked list data structure."""

    def __init__(self) -> None:
        """Initialize a singly circular linked list data structure."""
        self.tail = None  # First element in the list
        self.head = None  # Last element in the list
        self.count = 0

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

        current = self.tail
        for _ in range(index):
            current = current.next
        return current

    def __setitem__(self, index: int, value: Any) -> None:
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

        current = self.tail
        for _ in range(index):
            current = current.next
        current.data = value

    def __len__(self) -> int:
        """The length of the list."""
        return self.count

    def append(self, data: Any) -> None:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : Any
            The data to append to the list.
        """
        new_node = Node(data)
        if self.head:
            self.head.next = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.count += 1

    def clear(self) -> None:
        """Clear the list."""
        self.tail = self.head = None
        self.count = 0

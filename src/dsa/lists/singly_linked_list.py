from typing import Generator, Any


class Node:
    """Represent a node in a singly linked list."""

    def __init__(self, data: Any) -> None:
        """
        Initialize a node with the given data.

        Parameters
        ----------
        data : Any
            The data to be stored in the node.
        """
        self.data = data
        self.next = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"Node <data={self.data} next={self.next}>"

    def __repr__(self) -> str:
        """Return a string representation of the node for debugging purposes."""
        return f"Node(data={self.data})"


class SinglyLinkedList:
    """Represent a singly linked list data structure."""

    def __init__(self) -> None:
        """Initialize a singly linked list data structure."""
        self.tail = None
        self.head = None
        self.count = 0

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Return an iterator over the elements of the list.

        Yields
        ------
        Any
            The data of each node in the list.
        """
        current = self.tail
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

        current = self.tail
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Sets the data at the specified index in the list.

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

    def append(self, data: Any) -> None:
        """
        Append a new node with the given data to the end of the list.

        Parameters
        ----------
        data : Any
            The data to append to the list.
        """
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def delete(self, data: Any) -> None:
        """
        Delete the first occurrence of the specified data from the list.

        Parameters
        ----------
        data : Any
            The data to delete from the list.
        """
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                elif current == self.head:
                    previous.next = current.next
                    self.head = previous
                else:
                    previous.next = current.next
                self.count -= 1
                break
            previous = current
            current = current.next

    def search(self, data: Any) -> bool:
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

    def clear(self) -> None:
        """Clear the list."""
        self.tail = self.head = None
        self.count = 0


if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)

    sll.delete(5)

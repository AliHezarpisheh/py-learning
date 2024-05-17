"""Module containing Circular Linked Lists."""

from typing import Any, Generator, Optional


class Node:
    def __init__(
        self,
        data: Optional[Any] = None,
        next: Optional["Node"] = None,
        previous: Optional["Node"] = None,
    ) -> None:
        """Doubly Linked List Node."""
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

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Return an iterator over the elements of the list.

        Yields
        ------
        Any
            The data of each node in the list.
        """
        if self.tail is None:
            return

        current = self.tail
        while True:
            data = current.data
            yield data
            current = current.next
            if current == self.tail:
                break

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
        new_node = Node(data)
        if self.head:
            self.head.next = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.head.next = self.tail
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
                    self.head.next = self.tail
                elif current == self.head:
                    self.head = previous
                    self.head.next = self.tail
                else:
                    previous.next = current.next
                self.count -= 1
                break
            previous = current
            current = current.next

    def clear(self) -> None:
        """Clear the list."""
        self.tail = self.head = None
        self.count = 0


class DoublyCircularLinkedList:
    """Represent a doubly circular linked list data structure."""

    def __init__(self) -> None:
        """Initialize a doubly circular linked list data structure."""
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
        current = self.tail
        while True:
            data = current.data
            yield data
            current = current.next
            if current == self.head:
                break

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
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = new_node
            self.head.previous = new_node
        else:
            new_node.previous = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.previous = new_node
            self.tail = new_node
        self.count += 1

    def remove(self, data: Any) -> None:
        """
        Delete the first occurrence of the specified data from the list.

        Parameters
        ----------
        data : Any
            The data to delete from the list.
        """
        current = self.head
        is_deleted = False

        if current is None:
            pass
        elif current.data == data:
            self.head = self.tail = None
            is_deleted = True
        elif self.tail.data == data:
            self.tail = self.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            is_deleted = True
        else:
            while current:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    is_deleted = True
                    break
                current = current.next

        if is_deleted:
            self.count -= 1

    def reverse_iter(self) -> Generator[Any, None, None]:
        """Iterate in the reverse order of the list."""
        if self.tail is None:
            return

        current = self.tail
        while True:
            data = current.data
            yield data
            current = current.next
            if current == self.tail:
                break

    def clear(self) -> None:
        """Clear the list."""
        self.tail = self.head = None
        self.count = 0


if __name__ == "__main__":
    sll = SinglyCircularLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)

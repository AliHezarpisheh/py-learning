from typing import Any


class ListQueue:
    """Represent a queue data structure implemented with a list."""

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, data: Any) -> None:
        """
        Add data to the end of the queue.

        Parameters
        ----------
        data : Any
            The data to add to the queue.
        """
        self.items.insert(0, data)

    def dequeue(self) -> Any | None:
        """
        Remove and return the data at the end of the queue.

        Returns
        -------
        Any or None
            The data at the end of the queue or None if the queue is empty.
        """
        if not self.items:
            return None

        return self.items.pop()

    def __len__(self) -> int:
        """The size of the queue."""
        return len(self.items)

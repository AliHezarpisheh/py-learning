"""Module containing Stack Based Queue."""

from typing import Any

from ..stacks.node_stack import NodeStack


class StackBasedQueue:
    """Queue implemented using two stacks."""

    def __init__(self) -> None:
        """Initialize empty queue."""
        self.inbound_stack = NodeStack()
        self.outbound_stack = NodeStack()

    def enqueue(self, data: Any) -> None:
        """
        Enqueue an item.

        Parameters
        ----------
        data : Any
            The data to be enqueued.
        """
        self.inbound_stack.push(data)

    def dequeue(self) -> Any:
        """
        Dequeue an item.

        Returns
        -------
        Any
            The data from the front of the queue.
        """
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.push(self.inbound_stack.pop())

        return self.outbound_stack.pop()

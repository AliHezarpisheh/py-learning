"""
Monotonic Stacks

This module provides educational implementations of monotonic stacks,
which are specialized stack data structures used in various algorithmic problems.

Monotonic stacks maintain elements in a strictly increasing or decreasing order,
allowing efficient computation for problems like:

- Next Greater Element (NGE)
- Stock Span Problem
- Daily Temperatures
- Trapping Rain Water
- Largest Rectangle in Histogram

There are two types:
- **IncreasingStack**: Maintains elements in monotonically increasing order
    (i.e., smallest on bottom, largest on top).
- **DecreasingStack**: Maintains elements in monotonically decreasing order
    (i.e., largest on bottom, smallest on top).

When a new element violates the monotonic condition, the stack pops elements until the
condition is restored. This helps in tracking ranges, limits, or comparisons in linear
time.
"""

from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """Node class."""

    def __init__(self, data: T) -> None:
        """
        Initializes a new node with the given data.

        Parameters
        ----------
        data : T
            The data to be stored in the node.
        """
        self.data = data
        self.next = None


class IncreasingStack(Generic[T]):
    """A stack that maintains a monotonically increasing order."""

    def __init__(self) -> None:
        """Initialize a `DecreasingStack` instance."""
        self.stack = []

    def push(self, data: T) -> None:
        """
        Pushes an element onto the stack, maintaining increasing order.

        Parameters
        ----------
        data : T
            The element to be pushed onto the stack.
        """
        while self.stack and self.stack[-1] > data:
            self.stack.pop()
        self.stack.append(data)

    def pop(self) -> T | None:
        """
        Pops the top element from the stack.

        Returns
        -------
        T or None
            The popped element if the stack is not empty, else None.
        """
        return self.stack.pop() if self.stack else None

    def peek(self) -> T | None:
        """
        Returns the top element without removing it.

        Returns
        -------
        T or None
            The top element if the stack is not empty, else None.
        """
        return self.stack[-1] if self.stack else None

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.

        Returns
        -------
        int
            The size of the stack.
        """
        return len(self.stack)


class DecreasingStack(Generic[T]):
    """A stack that maintains a monotonically decreasing order."""

    def __init__(self) -> None:
        """Initialize a `DecreasingStack` instance."""
        self.stack = []

    def push(self, data: T) -> None:
        """
        Pushes an element onto the stack, maintaining decreasing order.

        Parameters
        ----------
        data : T
            The element to be pushed onto the stack.
        """
        while self.stack and self.stack[-1] < data:
            self.stack.pop()
        self.stack.append(data)

    def pop(self) -> T | None:
        """
        Pops the top element from the stack.

        Returns
        -------
        T or None
            The popped element if the stack is not empty, else None.
        """
        return self.stack.pop() if self.stack else None

    def peek(self) -> T | None:
        """
        Returns the top element without removing it.

        Returns
        -------
        T or None
            The top element if the stack is not empty, else None.
        """
        return self.stack[-1] if self.stack else None

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.

        Returns
        -------
        int
            The size of the stack.
        """
        return len(self.stack)

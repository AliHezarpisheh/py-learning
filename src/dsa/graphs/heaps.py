"""
A heap is a specialized tree-based data structure that satisfies the heap 
property. In a max heap, for any given node C, the value of C is less than 
or equal to the value of its parent P, with the highest value element at the 
root. Conversely, in a min heap, the value of P is less than or equal to the 
value of C, with the lowest value element at the root. Heaps are commonly 
implemented using arrays where the parent-child relationship can be 
determined through index calculations, making them efficient for priority 
queue operations. They support efficient insertion, deletion, and access to 
the highest or lowest value, typically in logarithmic time. Heaps are widely 
used in algorithms like heapsort for sorting data, as well as in graph 
algorithms like Dijkstra's and Prim's for finding the shortest path and 
minimum spanning tree, respectively.
"""

from typing import Any


class MinHeap:
    """A min-heap data structure implementation."""

    def __init__(self) -> None:
        """
        Initialize a new MinHeap.

        Creates an empty heap with a dummy element at index 0.
        """
        self.heap = [0]
        self.size = 0

    def insert(self, item: Any) -> None:
        """
        Insert a new item into the heap.

        Parameters
        ----------
        item : Any
            The item to be inserted into the heap.
        """
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def arrange(self, k: int) -> None:
        """
        Arrange the heap to maintain the heap property after insertion.

        Parameters
        ----------
        k : int
        The index of the newly inserted item to be arranged.
        """
        while k // 2 > 0:
            if self.heap[k // 2] > self.heap[k]:
                self.heap[k // 2], self.heap[k] = self.heap[k], self.heap[k // 2]
            k // 2

    def pop(self) -> Any:
        """
        Remove and return the smallest item from the heap.

        Returns
        -------
        Any
            The smallest item in the heap.
        """
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def sink(self, k: int) -> None:
        """
        Sink the item at index `k` to maintain the heap property after removal.

        Parameters
        ----------
        k : int
            The index of the item to be sunk.
        """
        while k * 2 < self.size:
            mc = self.get_min_index(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def get_min_index(self, k) -> int:
        """
        Get the index of the smaller child of the item at index `k`.

        Parameters
        ----------
        k : int
            The index of the current item.

        Returns
        -------
        int
            The index of the smaller child.
        """
        if (k * 2) + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

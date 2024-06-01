"""
Heap Sort is a comparison-based sorting algorithm that utilizes a binary heap data
structure. It sorts an array by first constructing a max heap (for ascending order) or
a min heap (for descending order) from the elements. Once the heap is built, it
repeatedly removes the root element (which is the maximum element in a max heap or
minimum element in a min heap) and rebuilds the heap.
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

    def heap_sort(self) -> list[int]:
        """
        Sorts the elements of the heap in ascending order using heap sort.

        Returns
        -------
        list of int
            The sorted list of integers in ascending order.

        Notes
        -----
        Heap sort is an in-place sorting algorithm with a time complexity of O(n log n)
        for both  average and worst cases. It begins by building a max-heap from the
        input array and then  repeatedly extracts the maximum element from the heap and
        reconstructs the heap until all  elements have been sorted.

        Examples
        --------
        >>> heap = MinHeap()
        >>> heap.insert(4)
        >>> heap.insert(10)
        >>> heap.insert(1)
        >>> heap.insert(5)
        >>> sorted_list = heap.heap_sort()
        >>> print("Sorted list:", sorted_list)
        [1, 4, 5, 10]
        """
        sorted_list = []
        for _ in range(self.size):
            element = self.pop()
            sorted_list.append(element)
        return sorted_list


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(4)
    heap.insert(10)
    heap.insert(1)
    heap.insert(5)

    sorted_list = heap.heap_sort()
    print("Sorted list:", sorted_list)

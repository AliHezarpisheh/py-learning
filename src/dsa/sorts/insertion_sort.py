"""
Insertion Sort is a simple sorting algorithm that builds the final sorted array
(or list) one item at a time. It works by iterating through the list, removing one
element and inserting it into the correct position in the already sorted part of the
list.

Explanation of Insertion Sort Algorithm:
Concept: Insertion Sort iterates through an array, starting with the second
element (assuming the first element is trivially sorted).

Insertion: For each element, it compares it with the elements in the sorted
section (to its left), shifting the larger elements one position to the right until it
finds the correct position to insert the current element.

Sorting in Place: It sorts the array in place, meaning it does not require additional
memory other than a few variables for comparisons and temporary storage.

Time Complexity:

Best Case: O(n) when the array is already sorted.
Worst Case: O(n^2) when the array is sorted in reverse order.
Average Case: O(n^2).
"""


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the insertion sort algorithm.

    Parameters
    ----------
    arr : list of int
        The list of integers to be sorted.

    Returns
    -------
    list of int
        The sorted list of integers.

    Examples
    --------
    >>> insertion_sort([12, 11, 13, 5, 6])
    [5, 6, 11, 12, 13]

    Notes
    -----
    Insertion sort is a simple sorting algorithm that builds the final sorted array one
    item at a time. It is much less efficient on large lists than more advanced
    algorithms such as quicksort, heapsort, or merge sort. However, insertion sort
    provides several advantages:
    1. Simple implementation
    2. Efficient for (quite) small data sets
    3. More efficient in practice than most other simple quadratic (i.e., O(n^2))
       algorithms such as selection sort or bubble sort
    4. Stable; does not change the relative order of elements with equal keys
    5. In-place; only requires a constant amount O(1) of additional memory space
    """
    for i in range(1, len(arr)):
        key = arr[i]

        k = i - 1
        while k >= 0 and key < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = key


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Sorted array is:", arr)

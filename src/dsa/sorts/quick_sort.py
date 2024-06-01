"""
Quick Sort is a highly efficient comparison-based sorting algorithm. It works by
partitioning an array into two sub-arrays around a pivot element. It recursively sorts
each sub-array. The key steps in the Quick Sort algorithm are partitioning and recursive
sorting.

Key Characteristics:
Comparison-based: Quick Sort uses comparisons to sort elements.
In-place sorting: It typically requiresO(logn) extra space for recursive calls but does
sorting in-place.
Unstable: It does not maintain the relative order of equal elements without additional
logic.

Time Complexity:
Worst-case: 
O(n^2) (rare, occurs when the pivot is consistently the smallest or largest element)
Best-case: 
O(nlogn)
Average-case: 
O(nlogn)

Steps:

Partitioning:
Choose a pivot element from the array (often the last element). Rearrange the array so
that all elements less than the pivot are before it and all elements greater than the
pivot are after it. The pivot is now in its final sorted position.

Recursive Sorting:
Recursively apply the above steps to the sub-array of elements with smaller values and
separately to the sub-array of elements with greater values.

Base Case:
The recursion terminates when the sub-array length is 0 or 1, as they are inherently
sorted.
"""


def quick_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the quick sort algorithm.

    Parameters
    ----------
    arr : list of int
        A list of integers that needs to be sorted.

    Returns
    -------
    list of int
        The sorted list of integers in ascending order.

    Examples
    --------
    >>> quick_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> quick_sort([3, 0, 2, 5, -1, 4, 1])
    [-1, 0, 1, 2, 3, 4, 5]

    >>> quick_sort([])
    []
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        lesser_than_pivot = []
        higher_than_pivot = []

        for element in arr:
            if element > pivot:
                higher_than_pivot.append(element)
            else:
                lesser_than_pivot.append(element)

        return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(higher_than_pivot)


if __name__ == "__main__":
    example_array = [64, 25, 12, 22, 11]
    sorted_array = quick_sort(example_array)
    print("Sorted array:", sorted_array)

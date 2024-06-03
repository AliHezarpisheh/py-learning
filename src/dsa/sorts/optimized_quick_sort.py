"""Quick sort algorithm using median of medians algorithm for pivot selection."""


def find_median(arr: list[int]) -> int:
    """
    Find the median of a list of integers.

    This function sorts the input list and returns the median element.
    If the list has an odd number of elements, the middle one is returned.
    If the list has an even number of elements, the lower middle one is returned.

    Parameters
    ----------
    arr : list of int
        The list of integers from which to find the median.

    Returns
    -------
    int
        The median element of the list.
    """
    arr.sort()
    return arr[len(arr) // 2]


def median_of_median(arr: list[int], low: int, high: int) -> int:
    """
    Find the median of medians in a list of integers.

    This function recursively finds the median of medians for use as a pivot in 
    the Quickselect algorithm. It divides the list into groups of at most 5 elements,
    finds the median of each group, and recursively finds the median of those medians.

    Parameters
    ----------
    arr : list of int
        The list of integers from which to find the median of medians.
    low : int
        The starting index of the subarray.
    high : int
        The ending index of the subarray.

    Returns
    -------
    int
        The median of medians of the list.
    """
    if high - low <= 5:
        return find_median(arr[low:high + 1])

    medians = []
    for i in range(low, high + 1, 5):
        sub_right = i + 4 if i + 4 <= high else high
        medians.append(find_median(arr[i: sub_right + 1]))
    return median_of_median(medians, 0, len(medians) - 1)


def partition(arr: list[int], low: int, high: int, pivot: int) -> list[int]:
    """
    Partition the array for the quickselect algorithm using a given pivot.

    This function rearranges the elements in the array such that all elements
    less than or equal to the pivot are on the left, and all elements greater
    than the pivot are on the right. It then places the pivot in its correct position.

    Parameters
    ----------
    arr : list of int
        The array to be partitioned.
    low : int
        The starting index of the subarray to partition.
    high : int
        The ending index of the subarray to partition.
    pivot : int
        The pivot element around which to partition the array.

    Returns
    -------
    int
        The index of the pivot element after partitioning.
    """
    pivot_index = arr.index(pivot)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the quick sort algorithm with
    median of medians pivot selection.

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
    def _quick_sort(arr: list[int], low: int, high: int):
        if low < high:
            pivot = median_of_median(arr, low, high)
            pi = partition(arr, low, high, pivot)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    if len(arr) <= 1:
        return arr

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    example_array = [64, 25, 12, 22, 11]
    sorted_array = quick_sort(example_array)
    print("Sorted array:", sorted_array)

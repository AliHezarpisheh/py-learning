"""
The Median of Medians algorithm is a more sophisticated pivot selection method designed
to ensure better performance in Quick Select, particularly in worst-case scenarios. The
main goal is to choose a good pivot that guarantees a better balance between subarrays,
leading to improved efficiency.
"""


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


def quick_select(arr: list[int], low: int, high: int, k: int) -> int:
    """
    Find the k-th smallest element in an array using the Quickselect algorithm.

    This function recursively partitions the array and selects the k-th smallest
    element. It uses the median of medians method to choose a good pivot for
    partitioning.

    Parameters
    ----------
    arr : list of int
        The array from which to select the k-th smallest element.
    low : int
        The starting index of the subarray.
    high : int
        The ending index of the subarray.
    k : int
        The index (0-based) of the k-th smallest element to find.

    Returns
    -------
    int
        The k-th smallest element in the array.

    Notes
    -----
    If the array does not contain at least k+1 elements, the behavior is undefined.
    """
    if low <= high:
        pivot = median_of_median(arr, low, high)
        pi = partition(arr, low, high, pivot)
        if pi == k:
            return arr[pi]
        elif pi < k:
            return quick_select(arr, pi + 1, high, k)
        else:
            return quick_select(arr, low, pi - 1, k)
    return None


if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 11, 26]
    k = 3
    # Note: k is 0-based, so for the 3rd smallest element, k should be 2
    result = quick_select(arr, 0, len(arr) - 1, k - 1)
    print(f"The {k}-th smallest element is {result}")

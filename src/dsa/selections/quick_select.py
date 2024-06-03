"""Quick Select is an efficient algorithm for finding the k-th smallest element in an
unordered list. It is similar to Quick Sort and works on the principle of
divide-and-conquer.
"""


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the array for the quickselect algorithm.

    This function chooses the last element as the pivot, places the pivot element at its
    correct position in the sorted array, and places all smaller elements to the left of
    the pivot and all greater elements  to the right of the pivot.

    Parameters
    ----------
    arr : list of int
        The array to be partitioned.
    low : int
        The starting index of the subarray to partition.
    high : int
        The ending index of the subarray to partition.

    Returns
    -------
    int
        The index of the pivot element after partitioning.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select(arr: list[int], low: int, high: int, k: int) -> int:
    """
    Find the k-th smallest element in an array using the Quickselect algorithm.

    This function recursively partitions the array and selects the k-th smallest
    element.
    
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
        piv = partition(arr, low, high)
        if piv == k:
            return arr[piv]
        elif piv < k:
            return quick_select(arr, piv + 1, high, k)
        else:
            return quick_select(arr, low, piv - 1, k)
    return None


if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 11, 26]
    k = 3
    # Note: k is 0-based, so for the 3rd smallest element, k should be 2
    result = quick_select(arr, 0, len(arr) - 1, k - 1)
    print(f"The {k}-th smallest element is {result}")

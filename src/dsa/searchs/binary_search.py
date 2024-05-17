"""
Binary search is an efficient algorithm for finding an item from a sorted list of items.
It works by repeatedly dividing in half the portion of the list that could contain the
item, until you've narrowed down the possible locations to just one.

Here's a detailed explanation and implementation of binary search in Python:

Explanation:
Initial Setup: Start with two pointers, one at the beginning (left) and one at the end
              (right) of the list.
Middle Element: Calculate the middle index (mid) of the current range (left to right).

Comparison:
If the middle element is the target, return its index.
If the target is less than the middle element, adjust the right pointer to mid - 1 to
discard the right half.
If the target is greater than the middle element, adjust the left pointer to mid + 1 to
discard the left half.
Repeat: Repeat steps 2 and 3 until the pointers converge. If the target is not found,
return an indication that it doesn't exist in the list (e.g., -1).
"""


def binary_search(arr: list, target: int, low: int, high: int) -> int:
    """
    Perform a binary search to find the target value in a sorted array.
    
    Parameters
    ----------
    arr : list
        The sorted list of elements to search.
    target : int
        The value to search for.
    low : int
        The lower bound index of the list to start searching from.
    high : int
        The upper bound index of the list to end the search.

    Returns
    -------
    int
        The index of the target value in the list if found, otherwise -1.

    Examples
    --------
    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> target = 7
    >>> binary_search(arr, target, 0, len(arr) - 1)
    6

    >>> target = 11
    >>> binary_search(arr, target, 0, len(arr) - 1)
    -1
    """
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7

    result = binary_search(arr, target, 0, len(arr) - 1)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

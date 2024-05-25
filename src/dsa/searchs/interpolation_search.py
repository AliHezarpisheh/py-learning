"""
Interpolation search is an improved variant of binary search that works on uniformly
distributed sorted arrays. Instead of dividing the array into halves like binary search,
it uses a formula to probe the position of the target element. This formula estimates
the likely position of the target based on its value relative to the smallest and
largest elements in the array. This approach allows interpolation search to converge
faster to the target element, especially when the elements in the array are evenly
distributed.
"""


def get_nearest_mid(input_list: list, low: int, high: int, search_value: int) -> int:
    """
    Return the interpolated midpoint between low and high indices.

    This function calculates the midpoint between two indices using interpolation.

    Parameters
    ----------
    input_list : list
        A list of integers sorted in ascending order.
    low : int
        The lower index in the list.
    high : int
        The higher index in the list.
    search_value : int
        The value being searched in the list.

    Returns
    -------
    int
        The interpolated midpoint index.
    """
    return low + ((high - low) // (input_list[high] - input_list[low])) * (
        search_value - input_list[low]
    )


def interpolation_search(input_list: list, target: int) -> int:
    """
    Perform interpolation search to find the index of the target value in the list.

    This function implements interpolation search to find the index of a target value
    in a sorted list.

    Parameters
    ----------
    input_list : list
        A list of integers sorted in ascending order.
    target : int
        The value being searched in the list.

    Returns
    -------
    int
        The index of the target value in the list, or -1 if not found.
    """
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = get_nearest_mid(input_list, low, high, target)
        if input_list[mid] == target:
            return mid
        elif input_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6

    result = interpolation_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

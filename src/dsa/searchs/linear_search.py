"""
Linear search is a straightforward algorithm that sequentially checks each element in a
list until the target element is found or all elements have been checked. Starting from
the beginning, it compares each element with the target. If a match is found, it
returns the index of the element; otherwise, it continues until the end of the list,
returning -1 if the target is not present.
"""


def unordered_linear_search(unordered_list: list[int], specific_item: int) -> int:
    """
    Perform linear search on an unordered list to find `specific_item`.

    Parameters
    ----------
    unordered_list : list[int]
        The unordered list to search.
    specific_item : int
        The item to search for in the list.

    Returns
    -------
    int
        Index of `specific_item` in `unordered_list` if found, otherwise -1.
    """
    for index in range(len(unordered_list)):
        if unordered_list[index] == specific_item:
            return index
    return -1


def ordered_linear_search(ordered_list: list[int], term: int) -> int:
    """
    Perform linear search on an ordered list to find `term`.

    Parameters
    ----------
    ordered_list : list[int]
        The ordered list to search.
    term : int
        The item to search for in the list.

    Returns
    -------
    int
        Index of `term` in `ordered_list` if found, otherwise -1.
    """
    for index in range(len(ordered_list)):
        if ordered_list[index] == term:
            return index
        elif ordered_list[index] > term:
            return -1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(ordered_linear_search(arr, 2))

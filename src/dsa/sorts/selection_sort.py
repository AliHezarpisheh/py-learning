"""
Selection Sort is another simple comparison-based sorting algorithm. It works by
repeatedly selecting the smallest (or largest, depending on the order) element from the
unsorted portion of the list and swapping it with the first unsorted element. This
process is repeated, moving the boundary of the sorted and unsorted portions of the list
until the entire list is sorted.
"""


def selection_sort(unordered_list: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Parameters
    ----------
    unordered_list : list of int
        A list of integers that needs to be sorted.

    Returns
    -------
    list of int
        The sorted list of integers in ascending order.

    Examples
    --------
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> selection_sort([3, 0, 2, 5, -1, 4, 1])
    [-1, 0, 1, 2, 3, 4, 5]

    >>> selection_sort([])
    []
    """
    list_size = len(unordered_list)
    for i in range(list_size):
        min_index = i
        for j in range(i + 1, list_size):
            if unordered_list[min_index] > unordered_list[j]:
                min_index = j
        unordered_list[i], unordered_list[min_index] = (
            unordered_list[min_index],
            unordered_list[i],
        )
    return unordered_list


if __name__ == "__main__":
    example_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(example_array)
    print("Sorted array:", sorted_array)

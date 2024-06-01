"""
Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly
stepping through the list to be sorted, comparing each pair of adjacent items and
swapping them if they are in the wrong order. The pass through the list is repeated
until the list is sorted.
"""


def bubble_sort(unordered_list: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

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
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> bubble_sort([3, 0, 2, 5, -1, 4, 1])
    [-1, 0, 1, 2, 3, 4, 5]

    >>> bubble_sort([])
    []
    """
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        swapped = False
        for j in range(iteration_number - i):
            if unordered_list[j] > unordered_list[j + 1]:
                unordered_list[j], unordered_list[j + 1] = (
                    unordered_list[j + 1],
                    unordered_list[j],
                )
                swapped = True
        if not swapped:
            break

    return unordered_list


if __name__ == "__main__":
    example_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(example_array)
    print("Sorted array:", sorted_array)

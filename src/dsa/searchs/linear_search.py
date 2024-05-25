def unordered_linear_search(unordered_list: list[int], specific_item: int) -> int:
    for index in range(len(unordered_list)):
        if unordered_list[index] == specific_item:
            return index
    return -1


def ordered_linear_search(ordered_list: list[int], term: int) -> int:
    for index in range(len(ordered_list)):
        if ordered_list[index] == term:
            return index
        elif ordered_list[index] > term:
            return -1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(ordered_linear_search(arr, 2))

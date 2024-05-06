def linear_search(arr: list, specific_item: int) -> int:
    for index in range(len(arr)):
        if arr[index] == specific_item:
            return index
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(linear_search(arr, 2))

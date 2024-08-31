def hourglassSum(arr):
    len_arr = len(arr)
    sums_list = []
    for current_row_index in range(len_arr - 2):
        for column_index in range(len_arr - 2):
            current_sum = (
                arr[current_row_index][column_index]
                + arr[current_row_index][column_index + 1]
                + arr[current_row_index][column_index + 2]
                + arr[current_row_index + 1][column_index + 1]
                + arr[current_row_index + 2][column_index]
                + arr[current_row_index + 2][column_index + 1]
                + arr[current_row_index + 2][column_index + 2]
            )
            sums_list.append(current_sum)
    return max(sums_list)


if __name__ == "__main__":
    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [
        [1, 1, 1, 0, 0, 0],
        [4, 4, 4, 2, 2, 2],
        [6, 6, 6, 3, 3, 3],
        [10, 10, 10, 5, 5, 5],
        [14, 14, 14, 7, 7, 7],
        [16, 16, 16, 8, 8, 8],
    ]
    result = hourglassSum(arr)
    print(result)

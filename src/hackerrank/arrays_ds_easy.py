def reverseArray(a):
    reversed_array = []

    len_array = len(a)
    last_elm_index = len_array - 1
    for index in range(0, len_array):
        elm = a[last_elm_index - index]
        reversed_array.append(elm)
    return reversed_array


if __name__ == "__main__":
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)

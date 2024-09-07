def arrayManipulation(n: int, queries: list[list[int]]):
    arr = [0] * (n + 1)
    for sub_arr in queries:
        a, b, k = sub_arr
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k

    max_value = 0
    current_value = 0
    for value in arr:
        current_value += value
        if current_value > max_value:
            max_value = current_value
    return max_value


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

"""
Game of two stacks

https://www.hackerrank.com/challenges/game-of-two-stacks/problem
"""

from collections import deque


def twoStacks(maxSum: int, a: list[int], b: list[int]) -> int:
    a, b = deque(a), deque(b)
    sum_numbers = 0
    count_numbers = 0
    while a or b:
        top_a = a[0] if a else float("inf")
        top_b = b[0] if b else float("inf")
        number = a.popleft() if top_a <= top_b else b.popleft()

        if sum_numbers + number > maxSum:
            return count_numbers

        sum_numbers += number
        count_numbers += 1
    return count_numbers


if __name__ == "__main__":
    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        print(str(result) + "\n")

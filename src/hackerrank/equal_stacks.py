from collections import deque


# First version (too much operations)
def equalStacks(h1, h2, h3):  # noqa: F811
    height_h1 = sum(h1)
    height_h2 = sum(h2)
    height_h3 = sum(h3)
    while not (height_h1 == height_h2 == height_h3):
        highest_stack = max([h1, h2, h3], key=sum)
        if highest_stack:
            highest_stack.pop(0)

            height_h1 = sum(h1)
            height_h2 = sum(h2)
            height_h3 = sum(h3)
        else:
            return -1
    return sum(h1)


# Second version (not readable and pythonic)
def equalStacks(h1, h2, h3):  # noqa: F811
    height_h1 = sum(h1)
    height_h2 = sum(h2)
    height_h3 = sum(h3)
    while not (height_h1 == height_h2 == height_h3):
        max_height = max(height_h1, height_h2, height_h3)

        highest_stack: list[int] | None = None
        if max_height == height_h1:
            highest_stack = h1
        elif max_height == height_h2:
            highest_stack = h2
        else:
            highest_stack = h3

        if highest_stack:
            removed_num = highest_stack.pop(0)
            if height_h1 == max_height:
                height_h1 -= removed_num
            elif height_h2 == max_height:
                height_h2 -= removed_num
            else:
                height_h3 -= removed_num
        else:
            return -1
    return sum(h1)


# Third version (more readable and pythonic)
def equalStacks(h1, h2, h3):  # noqa: F811
    height_h1 = sum(h1)
    height_h2 = sum(h2)
    height_h3 = sum(h3)
    while not (height_h1 == height_h2 == height_h3):
        highest_stack, max_height = max(
            [(h1, height_h1), (h2, height_h2), (h3, height_h3)],
            key=lambda item: item[1],
        )

        if highest_stack:
            removed_num = highest_stack.pop(0)
            if height_h1 == max_height:
                height_h1 -= removed_num
            elif height_h2 == max_height:
                height_h2 -= removed_num
            else:
                height_h3 -= removed_num
        else:
            return -1
    return height_h1


# Fourth version (more readable and using dequeue `popleft` for O(1) time complexity)
def equalStacks(h1, h2, h3):  # noqa: F811
    h1, h2, h3 = deque(h1), deque(h2), deque(h3)
    height_h1, height_h2, height_h3 = sum(h1), sum(h2), sum(h3)

    while not (height_h1 == height_h2 == height_h3):
        if (height_h1 >= height_h2) and (height_h1 >= height_h3):
            height_h1 -= h1.popleft()
        elif (height_h2 >= height_h1) and (height_h2 >= height_h3):
            height_h2 -= h2.popleft()
        else:
            height_h3 -= h3.popleft()
    return height_h1


# Fifth version (Using sets for super clean and high performance)
def get_cumulative_heights(stack: list[int]) -> set[int]:
    result = set()
    total = 0

    for height in reversed(stack):
        total += height
        result.add(total)
    return result


def equalStacks(h1: list[int], h2: list[int], h3: list[int]) -> int:  # noqa: F811
    cumulative_heights_h1: set[int] = get_cumulative_heights(h1)
    cumulative_heights_h2: set[int] = get_cumulative_heights(h2)
    cumulative_heights_h3: set[int] = get_cumulative_heights(h3)
    return max(
        cumulative_heights_h1 & cumulative_heights_h2 & cumulative_heights_h3, default=0
    )


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)

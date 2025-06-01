"""
Next Greater Element

This module provides a solution to the Next Greater Element (NGE) problem for arrays. 
For each element in the input array, it finds the first element to its right that is 
greater than the current element. The solution uses a stack-based approach for 
optimal O(n) time complexity.

Key Concepts
-----------
- Monotonic Stack: The algorithm maintains a stack that keeps elements in decreasing 
  order from bottom to top, allowing efficient next-greater-element lookup.
- Right-to-Left Processing: By processing the array from right to left, we can 
  efficiently determine the next greater element for each position in a single pass.

Common Applications
------------------
- Stock span problems
- Histogram problems
- Memory management algorithms
- Compiler design (symbol table management)
"""


def next_right_greater_element(numbers: list[int]) -> list[int]:
    """
    The Next Greater Element problem involves finding, for each element in an array,
    the first element to its right that is greater than the current element. If no
    such element exists, we use -1 to indicate this.

    This problem is efficiently solved using a stack-based approach that processes
    the array from right to left, maintaining candidates for the next greater element.

    Algorithm Approach (Using Stack)
    -------------------------------
    1. Initialize:
       - A result array filled with -1 (default when no greater element is found)
       - An empty stack to track potential next greater elements

    2. Process from right to left:
       - For each element, pop from stack until we find a greater element
       - The top of stack becomes the next greater element for current
       - Push current element onto stack (as it may be next greater for others)

    3. Return the populated result array

    Time Complexity: O(n) - Each element is pushed and popped from stack exactly once
    Space Complexity: O(n) - For the stack and result storage

    Example Visualization
    ---------------------
    Input: [4, 5, 2, 25]
    Processing:
    Index 3 (25): Stack empty → -1, push 25
    Index 2 (2): 25 > 2 → 25, push 2
    Index 1 (5): 2 < 5 → pop 2, 25 > 5 → 25, push 5
    Index 0 (4): 5 > 4 → 5, push 4
    Result: [5, 25, 25, -1]
    """
    len_numbers = len(numbers)
    result = [-1] * len_numbers
    stack = []  # Holding potential greater next element

    for index in range(len_numbers - 1, -1, -1):
        while stack and stack[-1] <= numbers[index]:
            stack.pop()
        if stack:
            result[index] = stack[-1]
        stack.append(numbers[index])

    return result


def next_left_greater_element(numbers: list[int]) -> list[int]:
    """
    Finds the next greater element to the left for each element in the array.
    For each element, returns the first element to its left that is greater than it.
    If no such element exists, returns -1 for that position.

    Algorithm Approach (Using Stack)
    -------------------------------
    1. Initialize:
       - A result array filled with -1 (default when no greater element is found)
       - An empty stack to track potential next greater elements

    2. Process from left to right:
       - For each element, pop from stack until we find a greater element
       - The top of stack becomes the next greater element for current
       - Push current element onto stack (as it may be next greater for others)

    3. Return the populated result array

    Time Complexity: O(n) - Each element is pushed and popped from stack exactly once
    Space Complexity: O(n) - For the stack and result storage

    Example
    -------
    >>> next_left_greater_element([4, 5, 2, 25])
    [-1, -1, 5, -1]
    """
    len_numbers = len(numbers)
    result = [-1] * len_numbers
    stack = []

    for index in range(len_numbers):
        while stack and stack[-1] <= numbers[index]:
            stack.pop()
        if stack:
            result[index] = stack[-1]
        stack.append(numbers[index])

    return result


def next_right_greater_element_circular(numbers: list[int]) -> list[int]:
    """
    Finds the next greater element to the right for each element in a circular array.
    For each element, returns the first element to its right that is greater than it,
    wrapping around to the start of the array if needed. If no such element exists,
    returns -1 for that position.

    Algorithm Approach (Using Stack)
    -------------------------------
    1. Initialize:
       - A result array filled with -1 (default when no greater element is found)
       - An empty stack to track potential next greater elements

    2. Process from right to left (twice the length to handle circular case):
       - For each element, pop from stack until we find a greater element
       - The top of stack becomes the next greater element for current
       - Push current element onto stack (as it may be next greater for others)
       - Only update results during the first pass (i < len_numbers)

    3. Return the populated result array

    Time Complexity: O(n) - Each element is pushed and popped from stack at most twice
    Space Complexity: O(n) - For the stack and result storage

    Example
    -------
    >>> next_right_greater_element_circular([4, 5, 2, 25])
    [5, 25, 25, -1]
    """
    len_numbers = len(numbers)
    result = [-1] * len_numbers
    stack = []  # Holding potential greater next element

    for i in range((2 * len_numbers) - 1, -1, -1):
        index = i % len_numbers
        while stack and stack[-1] <= numbers[index]:
            stack.pop()
        if i < len_numbers:
            if stack:
                result[index] = stack[-1]
        stack.append(numbers[index])

    return result


def next_left_greater_element_circular(numbers: list[int]) -> list[int]:
    """
    Finds the next greater element to the left for each element in a circular array.
    For each element, returns the first element to its left that is greater than it,
    wrapping around to the end of the array if needed. If no such element exists,
    returns -1 for that position.

    Algorithm Approach (Using Stack)
    -------------------------------
    1. Initialize:
       - A result array filled with -1 (default when no greater element is found)
       - An empty stack to track potential next greater elements

    2. Process from left to right (twice the length to handle circular case):
       - For each element, pop from stack until we find a greater element
       - The top of stack becomes the next greater element for current
       - Push current element onto stack (as it may be next greater for others)
       - Only update results during the first pass (i < len_numbers)

    3. Return the populated result array

    Time Complexity: O(n) - Each element is pushed and popped from stack at most twice
    Space Complexity: O(n) - For the stack and result storage

    Example
    -------
    >>> next_left_greater_element_circular([4, 5, 2, 25])
    [25, -1, 5, -1]
    """
    len_numbers = len(numbers)
    result = [-1] * len_numbers
    stack = []

    for i in range((len_numbers * 2) - 1):
        index = i % len_numbers
        while stack and stack[-1] <= numbers[index]:
            stack.pop()
        if i < len_numbers:
            if stack:
                result[index] = stack[-1]
        stack.append(numbers[index])

    return result


if __name__ == "__main__":
    numbers = [1, 2, 1]
    print(next_left_greater_element_circular(numbers=numbers))

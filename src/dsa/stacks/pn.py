"""
Prefix (Polish Notation)
Operators come before operands

Traverse right → left

Push operands, pop two for each operator

Example:
["*", "+", "2", "1", "3"]
Means: (* (+ 2 1) 3) → 9
"""

from typing import Any


class Node:
    """Node class."""

    def __init__(self, data: Any) -> None:
        """
        Initializes a new node with the given data.

        Parameters
        ----------
        data : Any
            The data to be stored in the node.
        """
        self.data = data
        self.next = None


class Stack:
    """Implementation of a stack using linked list nodes."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self.top = None
        self.size = 0

    def push(self, data: Any) -> None:
        """
        Push an item onto the top of the stack.

        Parameters
        ----------
        data : Any
            The data to be pushed onto the stack.
        """
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.size += 1

    def pop(self) -> Any | None:
        """
        Remove and returns the item at the top of the stack.

        Returns
        -------
        Any or None
            The data of the item removed from the top of the stack, or None if the stack
            is empty.
        """
        if not self.top:
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self) -> Any:
        """
        Return the data of the item at the top of the stack without removing it.

        Returns
        -------
        Any or None
            The data of the item at the top of the stack, or None if the stack is empty.
        """
        if self.top:
            return self.top.data
        else:
            return None

    def __len__(self) -> int:
        """Return the siz of the stack."""
        return self.size

    def __bool__(self) -> bool:
        return self.size > 0


def evaluate_pn(expression: str) -> float:
    """
    Evaluate a Polish Notation (PN) expression and return the result.

    Parameters
    ----------
    expression : str
        A string representing a valid PN expression where:
        - Operands (numbers) and operators (+, -, *, /) are space-separated.

    Returns
    -------
    float
        The result of evaluating the PN expression.

    Raises
    ------
    ValueError
        If the expression is invalid or cannot be evaluated correctly.
    ZeroDivisionError
        If there is a division by zero in the expression.

    Notes
    -----
    This function evaluates the PN expression using a stack-based approach:
    - Operands are pushed onto the stack in reverse-order.
    - Operators pop operands from the stack, apply the operation, and push the result
      back.
    - After processing all tokens, the final result is popped from the stack.

    Examples
    --------
    >>> evaluate_pn("/ + + 5 6 10 2")
    10.5
    """
    stack = []
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    tokens = reversed(expression.split())
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        elif token in operators:
            num1 = stack.pop()
            num2 = stack.pop()
            operator_func = operators.get(token)
            result = operator_func(num1, num2)
            stack.append(result)
        else:
            raise ValueError(f"Invalid number or operator: {token}")

    assert len(stack) == 1, (
        f"The reverse polish expression is not formed correctly: {expression}"
    )
    return stack.pop()


if __name__ == "__main__":
    expression = "/ + + 5 6 10 2"
    result = evaluate_pn(expression)
    print(result)

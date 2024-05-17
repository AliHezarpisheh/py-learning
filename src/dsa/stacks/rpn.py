"""
Parsing a reverse Polish expression (RPN) involves evaluating expressions written in
postfix notation, where operators follow their operands. This type of expression
eliminates the need for parentheses to dictate operation order, making it
straightforward to parse using a stack-based approach.

Steps to Parse and Evaluate a Reverse Polish Expression
Initialize a Stack:

Use a stack to keep track of operands.
Read the Expression:

Process the expression from left to right.
Process Tokens:

For each token in the expression:
If the token is an operand (number):
Push it onto the stack.
If the token is an operator (+, -, *, /):
Pop the required number of operands from the stack.
Perform the operation.
Push the result back onto the stack.
Final Result:

After processing all tokens, the stack should contain exactly one element, which is the
result of the expression.
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


def evaluate_rpn(expression: str) -> float:
    """
    Evaluate a Reverse Polish Notation (RPN) expression and return the result.

    Parameters
    ----------
    expression : str
        A string representing a valid RPN expression where:
        - Operands (numbers) and operators (+, -, *, /) are space-separated.

    Returns
    -------
    float
        The result of evaluating the RPN expression.

    Raises
    ------
    ValueError
        If the expression is invalid or cannot be evaluated correctly.
    ZeroDivisionError
        If there is a division by zero in the expression.

    Notes
    -----
    This function evaluates the RPN expression using a stack-based approach:
    - Operands are pushed onto the stack.
    - Operators pop operands from the stack, apply the operation, and push the result
      back.
    - After processing all tokens, the final result is popped from the stack.

    Examples
    --------
    >>> evaluate_rpn("3 4 + 2 * 7 /")
    2.0
    >>> evaluate_rpn("5 1 2 + 4 * + 3 -")
    14.0
    """
    stack = Stack()
    operators = {"+", "-", "*", "/"}

    for token in expression.split():
        if token not in operators:
            stack.push(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                stack.push(operand1 + operand2)
            elif token == "-":
                stack.push(operand1 - operand2)
            elif token == "*":
                stack.push(operand1 * operand2)
            elif token == "/":
                stack.push(operand1 / operand2)

    return stack.pop()


if __name__ == "__main__":
    expression = "3 4 + 2 * 7 /"
    result = evaluate_rpn(expression)
    print(result)

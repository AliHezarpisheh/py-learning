"""
The Stock Span Problem is a financial problem where we have a series of daily price
quotes for a stock and need to calculate the span of the stock's price for all days.
The span of the stock's price on a given day is defined as the maximum number of
consecutive days (starting from today and going backward) for which the stock price
was less than or equal to today's price.

Solution Approach Using a Stack:
The problem can be efficiently solved using a stack that keeps track of indices of
previous days' prices. The stack helps in finding the nearest previous day with a
higher price, allowing us to calculate the span quickly.

Algorithm Steps:
1. Initialize a stack to keep track of indices and a result list to store spans.
2. Iterate through each price in the prices list:
   a. While the stack is not empty and the price at the top of the stack is less than
      or equal to the current price, pop from the stack.
   b. If the stack becomes empty, it means the current price is the highest so far,
      so the span is index + 1.
   c. Otherwise, the span is the difference between the current index and the index
      at the top of the stack.
   d. Push the current index onto the stack.
3. Return the result list containing all spans.

Time Complexity:
This approach runs in O(n) time where n is the number of days, as each index is pushed
and popped from the stack at most once.
"""


def get_stock_span_prices(prices: list[int]) -> list[int]:
    """
    Calculate the stock span for each day's price in the given list.

    The stock span for a given day's price is defined as the number of consecutive days
    (including the current day) before it where the price was less than or equal to the
    current day's price.

    Parameters
    ----------
    prices : list[int]
        A list of integers representing daily stock prices.

    Returns
    -------
    list[int]
        A list of integers representing the stock span for each corresponding day in the
        input prices list.

    Examples
    --------
    >>> get_stock_span_prices([100, 80, 60, 70, 60, 75, 85])
    [1, 1, 1, 2, 1, 4, 6]
    >>> get_stock_span_prices([20, 30, 15, 60, 45, 20, 100])
    [1, 2, 1, 4, 1, 1, 7]

    Notes
    -----
    - The span for the first day is always 1.
    - This implementation uses a stack-based approach for O(n) time complexity.
    - The stack stores indices of prices rather than the prices themselves for efficient
      span calculation.
    """
    len_prices = len(prices)
    result = [0] * len_prices
    stack = []

    for index in range(len_prices):
        while stack and prices[stack[-1]] <= prices[index]:
            stack.pop()

        if not stack:
            result[index] = index + 1
        else:
            result[index] = index - stack[-1]

        stack.append(index)


if __name__ == "__main__":
    prices = [20, 30, 15, 60, 45, 20, 100]
    print(get_stock_span_prices(prices=prices))

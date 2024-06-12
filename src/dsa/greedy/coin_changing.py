"""Module for coin changing problems."""


def coin_change_greedy(coins: list[int], amount: int) -> list[tuple[int, int]]:
    """
    Find the minimum number of coins to make up the given amount.

    Args:
        coins (list[int]): List of coin denominations.
        amount (int): Amount to make up.

    Returns:
        list[tuple[int, int]]: List of tuples of coin denomination and count.
                               If not possible, returns a string indicating so.
    """
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        count = amount // coin
        amount %= coin
        result.append((coin, count))
        if amount == 0:
            break

    if amount:
        return "Not possible to make the amount with the given coins"
    return result


def coin_change_dp(coins: list[int], amount: int) -> list[tuple[int, int]]:
    """
    Find the minimum number of coins to make up the given amount using dynamic
    programming.

    Args:
        coins (list[int]): List of coin denominations.
        amount (int): Amount to make up.

    Returns:
        list[tuple[int, int]]: List of tuples of coin denomination and count.
                               If not possible, returns a string indicating so.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    if dp[amount] == float("inf"):
        return "Not possible to make the amount with the given coins"
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = int(input("Enter the amount: "))

    change = coin_change_dp(coins, amount)
    print(change)

def factorial(number: int) -> int:
    assert number >= 0, "The number should be greater than or equal 0"

    if number == 0:
        return 1
    result = number * factorial(number - 1)
    return result


if __name__ == "__main__":
    result = factorial(12)
    print(result)

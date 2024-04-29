def get_last_digit(number: int) -> int:
    return abs(number) % 10


def sum_of_digits(number: int) -> int:
    if number < 10:
        return number

    last_digit = get_last_digit(number=number)
    result = last_digit + sum_of_digits(number=number // 10)
    return result


if __name__ == "__main__":
    result = sum_of_digits(9876)
    print(result)

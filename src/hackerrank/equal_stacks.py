def equalStacks(h1, h2, h3):
    all_numbers = []

    for number in h1:
        all_numbers.append(number)
    for number in h2:
        all_numbers.append(number)
    for number in h3:
        all_numbers.append(number)

    all_numbers = sorted(all_numbers)


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

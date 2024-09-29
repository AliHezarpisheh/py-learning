OPENING_BRACKETS = ["[", "{", "("]
CLOSING_BRACKETS = ["]", "}", ")"]

BRACKETS_MAPPING = {
    OPENING_BRACKETS[index]: CLOSING_BRACKETS[index]
    for index in range(len(OPENING_BRACKETS))
}


def isBalanced(s: str):
    stack = []
    brackets = [char for char in s]

    for bracket in brackets:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif bracket in CLOSING_BRACKETS:
            last_bracket = stack.pop()
            if BRACKETS_MAPPING.get(last_bracket, "") != bracket:
                return "NO"
        else:
            raise ValueError(f"Value out of range: {bracket}")

    if len(stack) == 0:
        return "YES"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)

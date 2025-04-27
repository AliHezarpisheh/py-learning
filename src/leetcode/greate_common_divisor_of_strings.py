from math import gcd


class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        assert len(str1) >= 1 and len(str2) <= 1000
        assert str1.isascii() and str2.isascii()

        pattern = ""
        shortest_str = str1 if len(str1) <= len(str2) else str2
        for character in shortest_str:
            pattern += character

            # Check if the pattern make the whole `str1` and `str`
            is_pattern_valid_for_str1 = not any(str1.split(pattern))
            is_pattern_valid_for_str2 = not any(str2.split(pattern))
            if is_pattern_valid_for_str1 and is_pattern_valid_for_str2:
                return pattern
        else:
            return ""


class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[: gcd(len(str1), len(str2))]


if __name__ == "__main__":
    str1 = input("str1: ")
    str2 = input("str2: ")
    print(Solution1().gcdOfStrings(str1=str1, str2=str2))

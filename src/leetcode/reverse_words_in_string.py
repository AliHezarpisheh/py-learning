class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)


if __name__ == "__main__":
    s = input("string: ")
    print(Solution().reverseWords(s=s))

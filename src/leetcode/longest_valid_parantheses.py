class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]
        longest_valid_parentheses = 0
        for index, character in enumerate(s):
            if character == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    longest_valid_parentheses = max(
                        longest_valid_parentheses, (index - stack[-1])
                    )
        return longest_valid_parentheses


if __name__ == "__main__":
    characters = "(()))())("
    result = Solution().longestValidParentheses(s=characters)
    print(result)

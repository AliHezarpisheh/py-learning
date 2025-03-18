class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)

        min_len_words = min(len_word1, len_word2)
        merged_string = ""

        # Iterate through the range of the shortest word indexes
        for number in range(min_len_words):
            merged_string += word1[number] + word2[number]

        # If the length of the words are the same, the `merged_string` is ready
        if len(word1) == len(word2):
            return merged_string

        # Otherwise, we should add the remaining characters of the longest word to the
        # end of the `merged_string`.
        longest_word = word1 if len(word1) >= len(word2) else word2

        # The remaining characters should start from the `length of the shortest word`
        # index. e.g. word1=aaaa word2=bb -> merged_string=aba + remaining_characters=
        # word2[2:] = aa
        remaining_characters = longest_word[min_len_words:]
        return merged_string + remaining_characters


if __name__ == "__main__":
    word1 = input("word1: ")
    word2 = input("word2: ")
    print(Solution().mergeAlternately(word1=word1, word2=word2))

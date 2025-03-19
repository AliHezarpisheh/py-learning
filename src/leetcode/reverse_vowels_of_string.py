VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowel_indexes = []
        consonants = []
        consonants_indexes = []

        for index, character in enumerate(s):
            if character in VOWELS:
                vowels.append(character)
                vowel_indexes.append(index)
            else:
                consonants.append(character)
                consonants_indexes.append(index)
        reversed_vowels = list(reversed(vowels))

        characters = list(zip(reversed_vowels, vowel_indexes)) + list(zip(consonants, consonants_indexes))
        ordered_characters = sorted(characters, key=lambda character: character[1])

        result = "".join([character[0] for character in ordered_characters])
        return result


if __name__ == "__main__":
    s = input("string: ")
    print(Solution().reverseVowels(s=s))

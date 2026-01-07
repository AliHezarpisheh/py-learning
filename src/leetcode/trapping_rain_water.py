class Solution:
    def trap(self, heights: list[int]) -> int:
        next_right_greatest_elements = (
            self.get_next_right_greatest_element(numbers=heights)
        )
        next_left_greatest_elements = (
            self.get_next_left_greatest_element(numbers=heights)
        )
        zip_elements = zip(
            heights,
            next_left_greatest_elements,
            next_right_greatest_elements
        )

        result = 0
        for height, left_greatest_element, right_greatest_element in zip_elements:
            total_accepted_bars = min(left_greatest_element, right_greatest_element)
            if total_accepted_bars != -1:
                bars = total_accepted_bars - height
                result += bars if bars > 0 else 0
        return result

    @staticmethod
    def get_next_right_greatest_element(numbers: list[int]) -> list[int]:
        length_numbers = len(numbers)
        result = [-1] * length_numbers
        greatest_element = -1

        for index in range(length_numbers - 1, -1, -1):
            num = numbers[index]
            result[index] = greatest_element
            greatest_element = num if num > greatest_element else greatest_element
        return result

    @staticmethod
    def get_next_left_greatest_element(numbers: list[int]) -> list[int]:
        length_numbers = len(numbers)
        result = [-1] * length_numbers
        greatest_element = -1

        for index in range(length_numbers):
            num = numbers[index]
            result[index] = greatest_element
            greatest_element = num if num > greatest_element else greatest_element
        return result


class Solution:
    def trap(self, heights: list[int]) -> int:
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        left_max = right_max = 0
        result = 0

        while left <= right:
            if heights[left] <= heights[right]:
                left_max = heights[left] if heights[left] > left_max else left_max
                result += left_max - heights[left]
                left += 1
            else:
                right_max = heights[right] if heights[right] > right_max else right_max
                result += right_max - heights[right]
                right -= 1
        return result


if __name__ == "__main__":
    heights = [0, 7, 1, 4, 6]
    result = Solution().trap(heights=heights)
    print(result)

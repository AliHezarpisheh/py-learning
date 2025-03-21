class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_index = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[zero_index], nums[index] = nums[index], nums[zero_index]
                zero_index += 1
        return nums


if __name__ == "__main__":
    numbers = list(map(int, input("numbers: ").split()))
    print(Solution().moveZeroes(nums=numbers))

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        available_places = 0
        for index, flower in enumerate(flowerbed):
            if flower == 1:
                continue

            if len(flowerbed) == 1:
                if (flowerbed[0] == 0) and (n == 1):
                    return True
                else:
                    return False

            if (index == 0) and (flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                available_places += 1
            elif (index == len(flowerbed) - 1) and (flowerbed[index - 1] == 0):
                flowerbed[index] = 1
                available_places += 1
            else:
                if (flowerbed[index - 1] == 0) and (flowerbed[index + 1]) == 0:
                    flowerbed[index] = 1
                    available_places += 1

            if available_places >= n:
                return True

        return False


if __name__ == "__main__":
    flowerbed = list(map(int, input("flowerbed: ").split()))
    n = int(input("n: "))
    print(Solution().canPlaceFlowers(flowerbed=flowerbed, n=n))

# Exercise 605: Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for flower in range(1, len(flowerbed)-1):
            if flowerbed[flower] == flowerbed[flower-1] == flowerbed[flower+1] == 0:
                flowerbed[flower] = 1
                n -= 1
        return n <= 0
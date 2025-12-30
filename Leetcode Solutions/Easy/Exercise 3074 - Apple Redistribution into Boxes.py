# Exercise 3074: Minimum Number of Boxes to Store Apples
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumapple = sum(apple)
        capacity.sort()
        result = 0
        n = len(capacity) - 1
        while (sumapple > 0):
            sumapple -= capacity[n]
            n -= 1
            result += 1
        return result

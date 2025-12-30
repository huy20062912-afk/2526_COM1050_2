# Exercise 875: Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            k = (left + right) // 2
            hours = sum((pile + k - 1) // k for pile in piles)
            if hours <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result 
            
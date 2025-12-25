# Exercise 3075: Maximize Happiness of Selected Children
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness.sort(reverse=True)
        for i in range (k):
            current = happiness[i] - i
            if current <= 0:
                break
            total += current
        return total
    

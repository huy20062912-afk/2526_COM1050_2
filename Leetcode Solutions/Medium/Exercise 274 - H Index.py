# Exercise 374: H-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(n):
            k = n - i 
            if citations[i] >= k:
                return k
        return 0
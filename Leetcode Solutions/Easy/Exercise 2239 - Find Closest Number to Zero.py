# Exercise 2239: Find Closest Number to Zero
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')
        result = None
        for num in nums:
            distance = abs(num)
            if distance < closest:
                closest = distance
                result = num
            if distance == closest:
                if num > result:
                    result = num
        return result
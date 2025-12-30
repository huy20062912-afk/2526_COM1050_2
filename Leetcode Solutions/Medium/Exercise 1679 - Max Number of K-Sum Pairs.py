# Exercise 1679: Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = 0
        y = len(nums) - 1
        z = 0
        while x < y:
            total = nums[x] + nums[y]
            if total < k:
                x += 1
            elif total > k:
                y -= 1
            else:
                z += 1
                x += 1
                y -= 1
        return z  
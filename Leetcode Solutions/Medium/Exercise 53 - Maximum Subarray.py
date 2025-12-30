# Exercise 53: Maximum Subarray Problem
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        cur_sum = 0
        max_sum = nums[0]
        while r < len(nums):
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
            r += 1
        return max_sum
    
# This algorithm uses Kadane's algorithm to find the maximum sum of a contiguous subarray in linear time.
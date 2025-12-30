# Exercise 55: Jump game
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        last_index = len(nums) - 1
        for i,num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        if max_reach >= last_index:
            return True
        
# This uses a greedy approach to determine if the last index of the array can be reached from the first index.
# It iterates through the array, updating the maximum reachable index at each step.
# Enumerate is to get both the index and the value of each element in the array.
# Before this solution (which i asked AI to improve, enumerate came from AI itself), I had a flawed code:

 # class Solution:
 #   def canJump(self, nums: List[int]) -> bool:
 #       max_reach = 0
 #       if len(nums) == 1 or nums[0] >= len(nums):
 #           return True
 #       for num in nums:
 #           i = nums.index(num)
 #           if i > max_reach:
 #               return False
 #           max_reach = max(max_reach, i + nums[i])
 #       if max_reach >= len(nums):
 #           return True
 
 # The flaw in this code is that using nums.index(num) will always return the first occurrence of num in the list,
 # which can lead to incorrect calculations of the index when there are duplicate values in the list.
 # For example: [2,3,1,1,4]
 # When the loop reaches the second '1', nums.index(1) will return 2 instead of 3,
 # causing the max_reach calculation to be incorrect.
 # This can lead to incorrect results, especially in cases where the array contains duplicate values.
 # The improved version using enumerate correctly tracks the current index in the loop.
 
 # First time using greedy approach though, so I had to ask AI for help to optimize my code.
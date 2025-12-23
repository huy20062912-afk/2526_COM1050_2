# Exercise 169: Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for i in nums[1:]:
            count += 1 if i == res else -1
            if count == 0:
                res, count = i, 1
        return res
    
#Doing the 2nd way cuz Leetcode is apparently being a dumb website and doesnt accept line 3 despite import list:
class Solution:
    def majorityElement(self, nums):
        res = nums[0] # Initialize the candidate for majority element
        count = 1 # Initialize the count for the candidate
        for i in nums[1:]: # Iterate through the list starting from the second element
            count += 1 if i == res else -1 # Increment or decrement the count based on whether the current element matches the candidate
            if count == 0: # If count reaches zero, we need to choose a new candidate
                res, count = i, 1 # Update the candidate and reset count
        return res

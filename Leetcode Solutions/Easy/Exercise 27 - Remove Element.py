# Exercise 27: Remove Element
from typing import List # I have to import this list, when uploaded to leetcode it will have this imported by default
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:

            nums.remove(val)

        return len(nums)
# Exercise 35: Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
            result = nums.index(target)
        else:
            result = nums.index(target)
        return result

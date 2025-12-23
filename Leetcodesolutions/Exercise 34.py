# Exercise 34: Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        if target in nums:
            start = 0
            number = nums.count(target)
            for i in range(number):
                found = nums.index(target, start)
                result.append(found)
                start = found + 1
            return [result[0], result[-1]] # Avoids situations where there is only one int in the list
        else:
            result.append(-1)
            result.append(-1)
        return result    
# Exercise 961: N Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        result = set()
        for i in nums:
            if i in result:
                return i
            else:
                result.add(i)
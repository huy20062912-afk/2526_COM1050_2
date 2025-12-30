# Exercise 287: Find the duplicate number
# Solution using a dictionary to count occurrences
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] = result[num] + 1
            else:
                result[num] = 1
        for x in result:
            if result[x] != 1:
                return x
# Another solution which should be faster(it was indeed faster): using a set to track seen numbers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set()
        for y in nums:
            if y not in x:
                x.add(y)
            else:
                return y
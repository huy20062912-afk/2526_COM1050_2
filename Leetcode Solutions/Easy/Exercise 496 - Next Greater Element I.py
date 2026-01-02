# Exercise 496: Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        for num in nums2:
            while stack and num > stack[-1]:
                waiting_num = stack.pop()
                mapping[waiting_num] = num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(mapping.get(num,-1))
        return result
# Fundamental of stacks.
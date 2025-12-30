# Exercise 238: Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L_arr = [1] * n 
        left_product = 1
        for i in range(n):
            L_arr[i] = left_product 
            left_product = left_product * nums[i]
        right_product = 1
        for i in range(n - 1 ,-1, -1):
            L_arr[i] = L_arr[i] * right_product 
            right_product = right_product * nums[i] 
        return L_arr
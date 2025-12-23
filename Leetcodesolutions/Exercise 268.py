class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = 0
        for i in range(n+1):
            expected_sum += i
        real_sum = 0
        for num in nums:
            real_sum += num
        return expected_sum - real_sum
    
# Algorithm behind this is to make 2 values which is expected sum and real sum.
# Expected sum calculates the sum from the desired list. 
# Real sum calculates the sum from the real list
# Results is the expected sum subtracting real sum
# Exercise 209: Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        final_result = float('inf')
        for right in range(len(nums)):
            current_number = nums[right]
            current_sum += current_number
            while current_sum >= target:
                window_length = right - left + 1
                if window_length < final_result:
                    final_result = window_length
                remove_number = nums[left]
                current_sum -= remove_number
                left += 1
        if final_result == float('inf'):
            return 0
        return final_result
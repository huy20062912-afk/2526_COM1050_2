# Exercise 167: Two sum 2: Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break
        result = [left + 1, right + 1]
        return result
    
# This uses two-pointer technique to find the two numbers that add up to the target in a sorted array.
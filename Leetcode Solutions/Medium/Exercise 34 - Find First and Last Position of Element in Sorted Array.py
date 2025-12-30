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
# This gives O(n) time complexity while we need to find a O(logn) time complexity:
# We will use binary search to find O(logN) time complexity:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    index = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return index

        left_index = binary_search(nums, target, True)
        right_index = binary_search(nums, target, False)
        
        return [left_index, right_index]
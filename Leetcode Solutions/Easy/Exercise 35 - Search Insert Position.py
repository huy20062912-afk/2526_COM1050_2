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
# Since the upper result doesnt give 0(log n) time complexity i came up w a binary search instead:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left 
    # Return left here because if target is not found, while loop will terminate when left > right
    # Left will be the index where target should be inserted to maintain sorted order
    # We return left as insert point
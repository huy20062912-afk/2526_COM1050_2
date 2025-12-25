# Exercise 80: Remove Duplicates from Sorted Array II (8616 ms LOOOL)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > 2:
                while num in nums:
                    nums.remove(num)
                nums.append(num)
                nums.append(num)
                nums.sort()
        return len(nums)
# Why is this code so slow?
# Because the count() and remove() methods both have O(n) time complexity,
# and they are called inside a loop that iterates over the list,
# resulting in an overall time complexity of O(n^3) in the worst case.
# A more efficient approach would be to use a two-pointer technique to achieve O(n) time complexity.
# Better solution using two-pointer technique:
class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
    
# This improved solution iterates through the list only once,
# maintaining a count of duplicates and writing valid elements to the front of the list,
# resulting in a time complexity of O(n).

# Explanation of the better solution:
# 1. We first check if the input list is empty. If it is, we return 0.
# 2. We initialize two variables: write_index to keep track of where to write the next valid element,
#    and count to count the occurrences of the current number.  
# 3. We iterate through the list starting from the second element.
# 4. For each element, we check if it is the same as the previous one.
#    - If it is, we increment the count. 
#    - If it is not, we reset the count to 1.
# 5. If the count is less than or equal to 2, we write the current element to the write_index position
#    and increment the write_index.
# 6. Finally, we return the write_index, which represents the length of the modified list without extra duplicates. 

# Another solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k < 2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
    
# This solution also uses a two-pointer technique but with a slightly different approach.
# It checks if the current element can be added based on the last two elements in the modified list.
# It ensures that no more than two duplicates are kept by comparing the current element
# with the element at position k-2.
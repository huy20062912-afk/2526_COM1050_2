# Exercise 15: 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        big = []     
        for x in range(len(nums)-2):
            y = x + 1
            z = len(nums) - 1
            minusx = nums[x] * -1
            if x > 0 and nums[x] == nums[x-1]:
                continue
            while y < z:
                current_sum = nums[y] + nums[z]
                if current_sum < minusx:
                    y += 1
                elif current_sum == minusx:
                    small = [nums[x], nums[y], nums[z]]
                    big.append(small)
                    y += 1
                    while y < z and nums[y] == nums[y-1]:
                        y += 1
                    z -= 1
                    while y < z and nums[z] == nums[z+1]:
                        z -= 1
                else:
                    z -= 1
        return big
    

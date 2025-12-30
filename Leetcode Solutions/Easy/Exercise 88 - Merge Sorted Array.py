#Exercise 88: Merge sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2 # Append nums2 elements to nums1
        nums1.sort() # Sort the merged array
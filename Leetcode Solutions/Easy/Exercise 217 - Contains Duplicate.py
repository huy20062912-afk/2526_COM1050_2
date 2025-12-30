# Exercise 217: Contains Duplicate: https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=vs1emkne

class Solution(object):
    def containsDuplicate(self, nums): # type nums: List[int]) -> type: bool
        cont = dict() # dictionary to count occurrences
        for x in nums: # iterate through each number in the list
            if cont.get(x) == None: # if the number is not in the dictionary
                cont[x] = 1 # add it with count 1
            else: # if the number is already in the dictionary
                return True # duplicate found
        return False # no duplicates found
        
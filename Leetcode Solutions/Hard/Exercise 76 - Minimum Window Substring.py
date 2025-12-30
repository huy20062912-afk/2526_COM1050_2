# Exercise 76: Minimum Window Substring
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        dict_t = Counter(t)
        x = 0 
        y = len(dict_t)
        window = {}
        left = 0
        min_len = float('inf') 
        indexthatstart = 0
        for right in range(len(s)):
            new_letter = s[right]
            window[new_letter] = window.get(new_letter, 0) + 1
            if new_letter in dict_t and window[new_letter] == dict_t[new_letter]:
                x += 1
            while x == y:
                remove_letter = s[left]
                if remove_letter in dict_t and window[remove_letter] == dict_t[remove_letter]:
                    x -= 1
                window[remove_letter] -= 1
                current_len = right - left + 1       
                if min_len > current_len:
                    min_len = current_len
                    indexthatstart = left
                left += 1
        if min_len == float('inf'):
            return ""
        return s[indexthatstart:indexthatstart + min_len]
    
# Some bigass Explanation(I used AI here to assist me w code :sob:):
# I used counter on the t string to return the frequency of each letter on s
# I created another dictionary that represents the window
# The x here represents on whether a letter w the same frequency is in the window.
# If a value hits the same frequency, x will plus 1
# If x hits y, which is the length of the dictionary,
# We will check the while loop.
# We will remove letter from the left side
# If we removed a letter that is essential in the t string, x will minus one, which breaks the loop
# Update the current length of the window
# We placed a min_len initially of infinity so if we find a shorter length, we will update
# This is better than initially placing min_len of 0
# Because we cant find the shorter one later one
# Update the index that starts on the left side
# Finally we move the left side of the window by 1 step up
# After that we will find a string that starts with the indexthatstart
# And it ends with indexthatstart + min_len
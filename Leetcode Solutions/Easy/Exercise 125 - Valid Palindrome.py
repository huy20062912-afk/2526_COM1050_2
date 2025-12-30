# Exercise 125: Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lows = s.lower()
        oglist = list(lows)
        newlist = []
        for char in oglist:
            if char.isalnum():
                newlist.append(char)
        newstr = "".join(newlist)
        if newstr == newstr[::-1]:
            return True
        else:
            return False
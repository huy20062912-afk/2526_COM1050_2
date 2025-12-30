# Exercise 392: Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        y = len(s)
        for i in t:
            if x < y:
                if i == s[x]:
                    x += 1
        if x == y:
            return True
        else:
            return False
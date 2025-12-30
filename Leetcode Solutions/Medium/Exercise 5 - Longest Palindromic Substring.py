# Exercise 5: Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        final_res = ""
        for i in range(len(s)):
            current_res = s[i]
            l = i - 1
            r = i + 1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    current_res = s[l] + current_res + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            if len(final_res) < len(current_res):
                final_res = current_res
            if ( i!= len(s)-1 and s[i] == s[i+1]):
                current_res=s[i]+s[i+1]
                l = i - 1
                r = i + 2
                while l >= 0 and r <= len(s) - 1:
                    if s[l] == s[r]:
                        current_res = s[l] + current_res + s[r]
                        l -= 1
                        r += 1
                    else:
                        break
            if len(final_res) < len(current_res):
                final_res = current_res
        return final_res
# This algorithm checks for every elements in the string
# There are 2 cases to consider:
# 1. Odd length palindromes where the center is a single character
# 2. Even length palindromes where the center is between two characters
# If it falls for case 1, it expands outwards from the center character
# If it falls for case 2, it expands outwards from the center two characters
# Exercise 383: Ransom note
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        for i in count1:
            if count1[i] > count2[i]:
                return False
        return True

# This uses Counter to correct frequencies of characters in both strings and compares them.
# If any character in ransomNote has a higher frequency than in magazine, return False.

# I formerly used another approach:
#         for i in ransomNote:
#           if count1[i] <= count2[i]:
#                return True
#            else:
#                return False 

# This has a major flaw: it returns after checking only the first character, which can lead to incorrect results.
# I ended up returning True if the first character was found enough times, without checking the rest.
# Ended up having to ask Ai for help :sob:
# This is my 2nd time using Counter, and I am starting to get the hang of it!
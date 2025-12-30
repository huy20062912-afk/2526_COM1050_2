# Exercise 890: Find and Replace Pattern
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            a = {}
            b = {}
            is_match = True
            if len(word) != len(pattern):
                return False
            for x, y in zip(pattern, word):
                if x not in a and y not in b:
                    a[x] = y
                    b[y] = x
                elif x in a and a[x] != y:
                    is_match = False
                elif y in b and b[y] != x:
                    is_match = False
                else:
                    continue
            if is_match == True:
                res.append(word)
        return res
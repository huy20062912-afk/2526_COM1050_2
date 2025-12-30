# Exercise 151: Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        y = x [::-1]
        z = " ".join(y)
        return z
        
# Leetcode exercise 70: Climbing stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b  =  0, 1
        for i in range (n - 1):
            a, b = b, a + b
        k = a + b
        return k

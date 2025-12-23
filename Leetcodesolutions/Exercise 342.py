# Exercise 342: Power of four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or n == 2 or n & (n-1) != 0:
            return False
        elif n % 3 == 1 :
            return True
        else:
            return False
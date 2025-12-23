# Exercise 231: Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif 2 ** 31 % n == 0 :
            return True
        else:
            return False

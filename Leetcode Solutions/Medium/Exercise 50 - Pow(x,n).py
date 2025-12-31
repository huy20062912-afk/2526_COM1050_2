# Exercise 50: Pow(x,n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# This is such a stupid ass solution so i came w recursion solution:
class Solution:
    def Pow(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        tmp = self.Pow(x, n // 2)
        if n % 2 == 0:
            return tmp * tmp
        else:
            return tmp * tmp * x
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        return self.Pow(x,n)
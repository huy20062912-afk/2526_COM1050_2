# Exercise 367: Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            mid = (l+r) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
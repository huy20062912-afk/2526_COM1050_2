# Exercise 66: Plus one: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range (n-1, -1, -1):
            if digits[i] != 9:
                digits [i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0,1)
        return digits
# More of a brute force solution because im dumb asf:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = "".join(map(str, digits))
        integers = int(strings)
        plusone = integers + 1
        plus1 = str(plusone)
        res = [int(digit) for digit in plus1]
        return res
# Exercise 7: Reverse integer

class Solution:
    def reverse(self, x: int) -> int:
        k = list(str(x))
        k.reverse()
        if k[-1] == "-":
            k.pop()
            k.insert(0, "-")
        while k and k[0] == "0":
            k.pop(0)
        if not k:
            return 0
        result = "".join(k)
        intresult = int(result)
        if intresult < -2147483648 or intresult > 2147483647:
            return 0
        return intresult


        
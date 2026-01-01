# Exercise 20: Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        result_list = []
        opening = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for i in s:
            if i in '[{(':
                result_list.append(i)
            else:
                if not result_list or result_list[-1] != opening[i]:
                    return False
                result_list.pop()
        return not result_list

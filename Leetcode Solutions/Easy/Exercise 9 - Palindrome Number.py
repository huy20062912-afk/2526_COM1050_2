# Exercise 9: https://leetcode.com/problems/palindrome-number/ 

class Solution: # Định nghĩa lớp Solution
    def isPalindrome(self, x: int) -> bool: # Định nghĩa phương thức isPalindrome với tham số x kiểu int và trả về kiểu bool
        s = str(x) # Chuyển đổi số nguyên x thành chuỗi và gán cho biến s
        if s == s[::-1]: # Kiểm tra nếu chuỗi s bằng với chuỗi s đảo ngược
            return True
        else: 
            return False 
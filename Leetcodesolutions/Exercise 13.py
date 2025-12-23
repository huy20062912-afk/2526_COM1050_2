# Exercise 13: https://leetcode.com/problems/roman-to-integer/

class Solution: 
    def romanToInt(self, s: str) -> int: # Định nghĩa phương thức romanToInt với tham số s kiểu str và trả về kiểu int
        roman_map = { # Bảng ánh xạ ký tự La Mã sang giá trị số nguyên tương ứng
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500,
            'M': 1000
        }

        total = 0 # Biến lưu trữ tổng giá trị số nguyên
        n = len(s) # Độ dài của chuỗi s

        for i in range(n):
            current_val = roman_map[s[i]] # Lấy giá trị số nguyên tương ứng với ký tự La Mã hiện tại
            # Kiểm tra nếu ký tự hiện tại có giá trị nhỏ hơn ký tự tiếp theo
            # Nếu đúng, trừ đi giá trị hiện tại khỏi tổng, ngược lại cộng vào tổng
            if i < n - 1 and current_val < roman_map[s[i+1]]: # Kiểm tra điều kiện
                total -= current_val # Trừ giá trị hiện tại khỏi tổng
            else:
                total += current_val # Cộng giá trị hiện tại vào tổng
        return total
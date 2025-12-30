# Exercise 14: https://leetcode.com/problems/longest-common-prefix/

from ast import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # Định nghĩa phương thức longestCommonPrefix với tham số strs kiểu List[str] và trả về kiểu str
        minstr = min(strs, key = len) # Tìm chuỗi có độ dài ngắn nhất trong danh sách strs
        result = "" # Biến lưu trữ tiền tố chung dài nhất
        for i in range(len(minstr)): # Duyệt từng ký tự trong chuỗi ngắn nhất
            char = minstr[i] # Lấy ký tự hiện tại
            for s in strs: # Duyệt từng chuỗi trong danh sách strs
                if s[i] != char: # Kiểm tra nếu ký tự hiện tại không khớp với ký tự trong chuỗi s
                    return result # Trả về tiền tố chung dài nhất tìm được
            result += char # Thêm ký tự hiện tại vào tiền tố chung dài nhất
                if not strs: 
                    return "" # Trả về chuỗi rỗng nếu danh sách strs rỗng
        return result # Trả về tiền tố chung dài nhất sau khi duyệt hết các ký tự

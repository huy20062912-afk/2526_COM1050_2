# Exercise 1: https://leetcode.com/problems/two-sum

from typing import List # Giúp máy tính hiểu list là gì

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n): # Tạo vòng lặp để duyệt từng phần tử trong mảng
            for j in range(i + 1, n): # Tạo vòng lặp để duyệt từng phần tử trong mảng bắt đầu từ phần tử tiếp theo của i
                if nums[i] + nums[j] == target: # Kiểm tra nếu tổng của hai phần tử bằng target
                    return [i, j]
        return [] # Trả về mảng rỗng nếu không tìm thấy cặp phần tử nào thỏa mãn yêu cầu
        
# Better solution using a dictionary:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # Sử dụng từ điển để lưu trữ các phần tử đã duyệt
        seen = {} # Tạo một từ điển rỗng để lưu trữ các phần tử đã duyệt
        for i, num in enumerate(nums): # Duyệt từng phần tử trong mảng cùng với chỉ số của nó
            kek = target - num # Tính toán phần tử cần tìm để đạt được target
            if kek in seen: # Kiểm tra nếu phần tử cần tìm đã được duyệt
                return [seen[kek], i] # Trả về chỉ số của hai phần tử
            seen[num] = i # Lưu trữ phần tử hiện tại vào từ điển với chỉ số của nó
        return [] # Trả về mảng rỗng nếu không tìm thấy cặp phần tử nào thỏa
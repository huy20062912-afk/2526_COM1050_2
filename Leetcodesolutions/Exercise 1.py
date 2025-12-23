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
        
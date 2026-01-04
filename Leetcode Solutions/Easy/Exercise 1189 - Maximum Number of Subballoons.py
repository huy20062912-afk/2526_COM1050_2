# Exercise 1189: Maximum Number of Subballons
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        result_list = set()
        text_freq = Counter(text)
        b_freq = text_freq['b']
        a_freq = text_freq['a']
        n_freq = text_freq['n']
        l_freq = text_freq['l'] // 2
        o_freq = text_freq['o'] // 2
        result_list.add(b_freq)
        result_list.add(a_freq)
        result_list.add(n_freq)
        result_list.add(l_freq)
        result_list.add(o_freq)
        return min(result_list)
# A cleaner way with help of AI
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Bước 1: Đếm tần suất xuất hiện của từng ký tự trong text
        text_freq = Counter(text)
        
        # Bước 2: Tìm "nút thắt cổ chai" (min)
        # Vì 'l' và 'o' xuất hiện 2 lần trong "balloon", ta cần chia nguyên cho 2 (// 2)
        # Các ký tự 'b', 'a', 'n' giữ nguyên
        return min(
            text_freq['b'], 
            text_freq['a'], 
            text_freq['n'], 
            text_freq['l'] // 2, 
            text_freq['o'] // 2
        )
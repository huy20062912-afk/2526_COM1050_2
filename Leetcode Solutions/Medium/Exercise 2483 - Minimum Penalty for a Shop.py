#Exercise 2483: Minimum Penalty for a Shop
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Bước 1: Tính penalty ban đầu tại giờ 0
        # (Giả sử đóng cửa luôn, thì bị phạt bằng tổng số khách 'Y')
        current_penalty = customers.count('Y')
        
        # Biến lưu trữ kết quả tốt nhất
        min_penalty = current_penalty
        best_hour = 0
        
        # Bước 2: Duyệt qua từng giờ mở cửa bằng enumerate
        for i, char in enumerate(customers):
            # Nếu giờ này có khách (Y):
            # Việc mở cửa giúp ta đón được khách -> Penalty giảm 1
            if char == 'Y':
                current_penalty -= 1
            # Nếu giờ này không có khách (N):
            # Việc mở cửa làm tốn phí -> Penalty tăng 1
            else:
                current_penalty += 1
            
            # Bước 3: So sánh và cập nhật kết quả tốt nhất
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                # Tại sao là i + 1? 
                # Vì index i là giờ ta vừa quyết định mở cửa.
                # Giờ đóng cửa sẽ là giờ ngay sau đó.
                best_hour = i + 1
                
        return best_hour
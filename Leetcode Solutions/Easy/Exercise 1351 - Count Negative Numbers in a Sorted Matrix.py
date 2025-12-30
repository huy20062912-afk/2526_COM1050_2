# Exercise 1351: Count Negative Numbers in a Sorted MatrixS
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Bắt đầu từ góc dưới cùng bên trái
        r = rows - 1
        c = 0
        
        count = 0
        
        # Điều kiện dừng: Khi robot đi ra khỏi biên trên hoặc biên phải
        while r >= 0 and c < cols:
            if grid[r][c] < 0:
                # Nếu gặp số âm:
                # 1. Tất cả các số bên phải nó cũng là âm -> Cộng dồn vào count
                count += (cols - c)
                # 2. Dòng này coi như xong, đi lên trên để xét dòng tiếp
                r -= 1
            else:
                # Nếu gặp số dương:
                # Đi sang phải để tìm số nhỏ hơn
                c += 1
                
        return count
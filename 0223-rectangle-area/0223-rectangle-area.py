class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
     
        x_end = min(bx2, ax2)
        x_start = max(ax1, bx1)
        
        y_start = max(ay1, by1)
        y_end = min(by2, ay2)
        overlap = 0
        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)
        if x_end > x_start and y_end > y_start:
            # print("a")
            overlap = (x_end - x_start) * (y_end - y_start)
        
        # print(overlap)
        return area_1 + area_2 - overlap
            
        
        
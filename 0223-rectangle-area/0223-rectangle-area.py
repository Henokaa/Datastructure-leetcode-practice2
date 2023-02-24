class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        width1 = ax2 - ax1
        height1 = ay2 - ay1
        rec1 = height1 * width1
        width2 = bx2 - bx1
        height2 = by2 - by1
        rec2 = width2 * height2
        
        x1 = max(ax1, bx1)
        y1 = max(by1, ay1)
        x2 = min(ax2,bx2)
        y2 = min(ay2, by2)
        
        x = x2 - x1
        y = y2 - y1
        overlap = 0
        if x > 0 and y > 0:
            overlap = x * y
        # print(rec1, rec2, x, y)
        ans = rec1 + rec2 - overlap
        return ans
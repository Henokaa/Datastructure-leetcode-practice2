class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1w = (ax1, ax2)
        rec2w = (bx1, bx2)
        disw = 0
        if rec1w[0] <= rec2w[0] <= rec1w[1] or rec2w[0] <= rec1w[0] <= rec2w[1]:
            disw = (max(ax1,bx1), min(ax2,bx2))
            disw = disw[1] - disw[0]
        
        rec1h = (ay1, ay2)
        rec2h = (by1, by2)
        
        dish = 0
        if rec1h[0] <= rec2h[0] <= rec1h[1] or rec2h[0] <= rec1h[0] <= rec2h[1]:
            dish = (max(ay1, by1),min(ay2, by2))
            # print(dish)
            dish = dish[1] - dish[0]
            
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        area = area1 + area2
        # print(area, dish, disw)
        return area - (dish * disw)
            
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, x2 = rec1[0], rec1[2]
        y1, y2 = rec1[1], rec1[3]

        count = 0
        if x1 < rec2[2] and rec2[0] < x2:
            count += 1
        if y1 < rec2[3] and rec1[3] > rec2[1]:
            count += 1

        if count == 2:
            return True
        return False
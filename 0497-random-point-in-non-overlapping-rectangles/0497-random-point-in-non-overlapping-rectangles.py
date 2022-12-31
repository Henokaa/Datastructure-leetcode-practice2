class Solution:

    def __init__(self, rects: List[List[int]]):
        total = 0
        self.rects = []
        
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
        
        self.total = total
        
        running_weight = 0
        for x1, y1, x2, y2 in rects:
            weight = ((x2-x1+1) * (y2 - y1 + 1)) / total
            running_weight += weight
            self.rects.append((running_weight, x1, y1, x2, y2))
        
    def pick(self) -> List[int]:
        r = random.random()
        for weight, x1, y1, x2, y2 in self.rects:
            if weight > r:
                x = random.randint(x1,x2)
                y = random.randint(y1,y2)
                
                return [x,y]
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
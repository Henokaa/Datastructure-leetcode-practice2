class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x1 = random.uniform(self.x - self.r, self.x + self.r)
            y1 = random.uniform(self.y - self.r, self.y + self.r)
            
            if (x1 - self.x) ** 2 + (y1 - self.y) ** 2 <= self.r ** 2:
                return [x1, y1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
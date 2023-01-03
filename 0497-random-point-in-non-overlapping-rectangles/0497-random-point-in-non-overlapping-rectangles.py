class Solution:

    def __init__(self, rects: List[List[int]]):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        print(w)
        total = 0
        self.weights = []
        for i in w:
            total += i
            self.weights.append(total)
        print(self.weights)
        self.rects = rects

        
            
        
    def pick(self) -> List[int]:
        rand = random.randint(1, self.weights[-1] - 1)
        n_rect = bisect.bisect(self.weights, rand)
        # print(rand, n_rect ,self.weights[n_rect])
        # print(n_rect, rand)
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]
        
        
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
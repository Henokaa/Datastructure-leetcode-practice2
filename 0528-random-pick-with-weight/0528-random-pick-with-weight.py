class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for i in w:
            total += i
            self.prefix.append(total)
        # print(self.prefix)
            
        

    def pickIndex(self) -> int:
        ran = random.randint(1,self.prefix[-1])
        l = -1
        r = len(self.prefix)
        
        while r > l + 1:
            mid = l + (r - l)//2
            if self.prefix[mid] == ran:
                return mid
            if self.prefix[mid] > ran:
                r = mid
            else:
                l = mid
        # print(ran,r)
        return r
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
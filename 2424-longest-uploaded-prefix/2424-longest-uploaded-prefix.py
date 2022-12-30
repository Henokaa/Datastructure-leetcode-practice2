class LUPrefix:

    def __init__(self, n: int):
        self.i = 1
        self.videos = []
        

    def upload(self, video: int) -> None:
        heapq.heappush(self.videos, video)

    def longest(self) -> int:
        # print(self.videos)
        while self.videos and self.i == self.videos[0]:
            heapq.heappop(self.videos)
            self.i += 1
        if self.i == 1:
            return 0
        else:
            return self.i - 1
            
        
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
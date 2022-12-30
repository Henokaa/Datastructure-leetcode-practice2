class StockPrice:

    def __init__(self):
        self.saved = {}
        self.maxHeap = []
        self.latest = 0
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.saved[timestamp] = price
        heapq.heappush(self.maxHeap, (-price, timestamp))
        heapq.heappush(self.minHeap, (price, timestamp))
        self.latest = max(self.latest, timestamp)
        
        

    def current(self) -> int:
        return self.saved[self.latest]
        

    def maximum(self) -> int:
        while self.maxHeap:
            pricex, timestamp =heapq.heappop(self.maxHeap)
            pricex = -pricex
            if self.saved[timestamp] == pricex:
                heapq.heappush(self.maxHeap, (-pricex, timestamp))
                return pricex
        
            
        
                
        

    def minimum(self) -> int:
        while self.minHeap:
            pricex, timestamp = heapq.heappop(self.minHeap)
            if self.saved[timestamp] == pricex:
                heapq.heappush(self.minHeap, (pricex, timestamp))
                return pricex
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
from sortedcontainers import SortedList
class StockPrice:
    def __init__(self):
        self.prices = {}
        self.s1 = SortedList()
        self.latest = (None, None)
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices:
            self.s1.remove(self.prices[timestamp])
        
        if self.latest[0] is None or timestamp >= self.latest[0]:
            self.latest = (timestamp, price)
        
        self.s1.add(price)
        self.prices[timestamp] = price
        
    def current(self) -> int:
        return self.latest[1]

    def maximum(self) -> int:
        return self.s1[-1]

    def minimum(self) -> int:
        return self.s1[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
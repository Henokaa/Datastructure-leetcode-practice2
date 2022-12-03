class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        total = 1
        if self.stack:
            while self.stack and self.stack[-1][0] <= price:
                temp = self.stack.pop()
                total += temp[1]
            self.stack.append((price, total))
            return total
        else:
            self.stack.append((price, total))
            return total 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        '''
        
        '''
        # sort
        stock = stockPrices
        # stock = sorted(stock, key = lambda x:x[0])
        stock.sort()
        print(stock)
        # prev slope and the comming slope must be same 
        l = 0
        r = 1
        count = 0
        dy = None
        dx = None
        while r < len(stock):
            y = stock[r][1] - stock[l][1]
            x = stock[r][0] - stock[l][0]
            
            if dy is None or y * dx != x * dy:
                count += 1
            dx = x
            dy = y
            r += 1
            l += 1
            
        return count
        # 
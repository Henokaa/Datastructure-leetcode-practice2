class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit =prices[r] - prices[l]
                maxp = max(maxp, profit)
                r +=1
            else:
                l = r
                r += 1
        return maxp
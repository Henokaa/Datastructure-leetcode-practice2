class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''[7,1,5,3,6,4]
                  ^ ^'''
        l = 0
        r = l + 1
        mx = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            mx += prices[r] - prices[l]
            l = r
            r += 1
        return mx
        
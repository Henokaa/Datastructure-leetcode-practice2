class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] *(amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    if a - c == 0:
                        dp[a] = 1  # +1 for that specific coin
                    else:
                        dp[a] = min(dp[a], dp[c] + dp[a - c]) 
                        '''it first start as a dp[a] = inf but then with the first coin it changes so doesn't work without min b/c it takes the min for every coin ''' 
                        # or 1 + dp[a - c]
        # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
    
    ''' TimeComplexity: o(amount * len(coins))
    space: o(n)'''
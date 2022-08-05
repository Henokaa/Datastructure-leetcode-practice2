class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] *(amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    if a - c == 0:
                        dp[a] = min(dp[a], 1 + dp[a - c])  # +1 for that specific coin
                    else:
                        dp[a] = min(dp[a], dp[c] + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    ''' TimeComplexity: o(amount * len(coins))
    space: o(n)'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            

            shortest = float('inf')
            for i in range(len(coins)):
                if target - coins[i] >= 0:
                        shortest = min(shortest, dp(target - coins[i]) + 1)
            memo[target] = shortest
            return shortest
        memo = {}
        ans = dp(amount)
        if ans == float('inf'):
            return  -1
        return ans
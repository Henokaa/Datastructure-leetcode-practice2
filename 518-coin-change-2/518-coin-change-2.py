class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(result,x):
            state = (result,x)
            if state in memo:
                return memo[state]
            
            if result == amount:
                return 1
            
            if result > amount or x >= len(coins):
                return 0
            
            shortest = dp(result+ coins[x], x)+ dp(result, x + 1)
            # for c in range(x, len(coins)):
            #     if (result + coins[c]) <= amount:
            #         shortest += dp(result + coins[c], c)
            memo[state] = shortest
            return shortest
        
        return dp(0, 0)
'''Bruteforce timecomplexity - ''' 
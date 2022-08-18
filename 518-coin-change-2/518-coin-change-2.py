class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        @cache
        def dp(result,x):
            
            if result == amount:
                return 1
            
            if result > amount:
                return 0
            
            shortest = 0
            for c in range(x, len(coins)):
                if (result + coins[c]) <= amount:
                    shortest += dp(result + coins[c], c)
            
            return shortest
        
        return dp(0, 0)
'''Bruteforce timecomplexity - '''
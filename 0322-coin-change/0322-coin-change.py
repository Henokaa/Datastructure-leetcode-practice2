class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        
        '''
        saved = {}
        def dp(num):
            if num in saved:
                return saved[num]
            if num == amount:
                return 0
            
            shortest = float("inf")
            for i in range(len(coins)):
                if coins[i] + num <= amount:
                    total = 1 + dp(coins[i] + num)
                    shortest = min(shortest, total)
                    
            saved[num] = shortest
            return shortest

        ans = dp(0)
        if ans == float("inf"):
            return -1
        return ans
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dfs(i):
            coins[i] + dfs(i)
            dfs(i+1)
        '''
        '''
        dfs(cur):
            small
            for i
                if cur + i < amount
                    temp = 1 + dfs(cur + i)
                min(small, )
        '''
        
        '''
        dp(total)
        # memoize - amount
        # route - return min
        
        '''
        saved = {}
        def dp(total):
            
            if total == amount:
                return 0
            
            if total in saved:
                return saved[total]
            
            minimum = float('inf')
            for i in range(len(coins)):
                if coins[i] + total <= amount:
                    path = 1 + dp(total + coins[i])
                    minimum = min(minimum ,path)
            
            saved[total] = minimum
            return minimum
            
            
        res = dp(0)
        if res == float('inf'):
            return -1
        return res
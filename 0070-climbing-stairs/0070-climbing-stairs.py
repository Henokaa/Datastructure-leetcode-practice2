class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            temp1 = 0
            temp2 = 0
            
            if i == n:
                return 1
            if i + 1 <= n:
                temp1 = dp(i+1)
            if i + 2 <= n:
                temp2 = dp(i+2)
            return temp1 + temp2
        
        return dp(0)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(x):
            if x in memo:
                return memo[x]
            if x==n: 
                return 1
            if x == n-1:
                return 1
            
            memo[x] = climb(x+1) + climb(x+2)
            return memo[x]
        return climb(0)
        
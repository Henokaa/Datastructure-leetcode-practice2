class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            x , y  = 0, 0
            if int(s[i]) != 0:
                x = dp(i+1)
                
            st = s[i:i+2]
            
            if i + 1 < len(s) and 10 <= int(st) <= 26:
                y = dp(i+2)
            memo[i] = x + y
            return x + y
        
        return dp(0)
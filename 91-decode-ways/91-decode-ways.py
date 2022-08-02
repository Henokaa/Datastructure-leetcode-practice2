# "025" is invalid because a string could not start with a zero
class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:   # whether it is cached or it is the last one
                return dp[i]
            if s[i] == "0":   #if it starts with 0 invalid
                return 0
            
            if len(s) == 1: #length not len(s) - 1because we will add i+1 when it gets here
                return 1  

            res = dfs(i + 1)
            if i + 1 <= len(s)-1 and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            # print(res)
            dp[i] = res
            return res
        x = dfs(0)
        print(dp)
        return x
        
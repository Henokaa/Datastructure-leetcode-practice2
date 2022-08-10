class Solution:
    def numDecodings(self, s: str) -> int:
        dicti = {}
        n = len(s)+1
        dp = [0]*n
        dp[n-1] = 1 
        # base case initialization
	
        
        for i in range(n-2,-1,-1):
            
            if 1<= int(s[i:i+1]) <= 9:
                dp[i] = dp[i+1]
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            
                
        return dp[0]
    
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     c = 0
        #     if 1 <= int(s[i]) <= 9:
        #         c += dfs(i+1)
        #     if 10 <= int(s[i:i+2]) <= 26:
        #         c += dfs(i+2)
        #     return c
        # return dfs(0)
        # 121
            
                
        
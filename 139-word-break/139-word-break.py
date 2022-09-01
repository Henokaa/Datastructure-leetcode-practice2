class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i]=dp[i+len(w)] # because there is a repetition in char its like + 1

                if dp[i]: # if one become successful end
                    break
        return dp[0]
                
        # time complexity - 0(n*m*n) the last n for comparing
        
        
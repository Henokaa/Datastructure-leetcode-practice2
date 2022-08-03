class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 2 <= len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
                
        print(dp)
        return dp[0]
    ''' TimeComplexity - o(n), space - o(n) but in this case you can use two variables and have the space down to o(1)'''
        
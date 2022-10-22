class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s) 
        dp = [[0] * ( n + 1) for _ in range(n + 1)]
        for i in range(n,-1,-1):
            for j in range(n + 1):
                if i > (j - 1):
                    continue 
                if s[i] == s[j - 1]:
                    if i == (j - 1):
                        dp[i][j] = 1 + dp[i + 1][j - 1]
                    else:
                        dp[i][j] =  2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j -1])
        return dp[0][n]
"""
def dp(i, j):
            if i > j:
                return 0
            if s[i] == s[j]:
                if i == j:
                    return 1 + dp(i + 1, j - 1)
                return 2 + dp(i + 1, j - 1)
            return max(dp(i + 1, j),
                        dp(i, j - 1))
        return dp(0, len(s) - 1)
    TopDown: 
        state: i,j 
            state exec order: i -> [0, n] 
                              j -> [n-1,-1] => [n,0] 0 -> -1, n-1 => n
        base case: i > j: 0
    i: 0 -> n 
    j: n - 1 -> -1 => shift => n -> 0 

    base case: 
        i > j => 0 
    #######
    i: n -> 0 
    j: 0 -> n 
"""
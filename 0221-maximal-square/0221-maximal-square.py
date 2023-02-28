class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for i in range(cols+1)] for i in range(rows+1)]
        
        for r in range(rows,-1,-1):
            for c in range(cols,-1,-1):
                if r >= rows or c >= cols or matrix[r][c] == '0':
                    continue
                else:
                    dp[r][c] = 1+min(dp[r+1][c], dp[r][c+1],dp[r+1][c+1])
                    res = max(res, dp[r][c])
                    
        return res**2
        
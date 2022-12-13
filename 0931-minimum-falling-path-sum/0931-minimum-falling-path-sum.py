class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inbound = lambda r,c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        memo = {}
        def dp(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            temp1 = float('inf')
            temp2 = float('inf')
            temp3 = float('inf')
            if inbound(x + 1,y):
                temp1 = dp(x + 1,y)
                temp1 = matrix[x][y] + temp1
            if inbound(x + 1, y - 1):
                temp2 = dp(x + 1, y - 1)
                temp2 = matrix[x][y] + temp2
            if inbound(x + 1, y + 1):
                temp3 = dp(x + 1, y + 1)
                temp3 = matrix[x][y] + temp3
            
            res = min(temp1, temp2, temp3)
            if res == float('inf'):
                memo[(x,y)] = matrix[x][y]
                return matrix[x][y]
            else:
                memo[(x,y)] = res
                return res
            
            
        
        ans = float('inf')
        
        for x in range(len(matrix)):
            value = dp(0,x)
            ans = min(ans, value)
            
        return ans
        
        
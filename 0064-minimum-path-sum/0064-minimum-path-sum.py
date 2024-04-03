class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            
            left = float('inf')
            if inbound(i+1,j):
                left = dfs(i+1, j)
            
            down = float('inf')
            if inbound(i, j+1):
                down = dfs(i, j + 1)
            memo[(i,j)] = grid[i][j] + min(left, down)
            return memo[(i,j)]

        m = len(grid)
        n = len(grid[0])
        memo = {}
        return dfs(0, 0)
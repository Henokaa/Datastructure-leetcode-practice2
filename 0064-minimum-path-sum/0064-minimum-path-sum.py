class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i == m - 1:
                memo[(i, j)] = grid[i][j] + dfs(i, j+1)
            elif j == n - 1:
                memo[(i, j)] = grid[i][j] + dfs(i+1, j)
            else:
                memo[(i, j)] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            return memo[(i, j)]

        m = len(grid)
        n = len(grid[0])
        memo = {}
        return dfs(0, 0)
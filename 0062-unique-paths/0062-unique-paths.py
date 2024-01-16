class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]
        print(grid)
        for i in range(m):
            for j in range(n):
                left = 0
                if j-1 >= 0:
                    left = grid[i][j-1]
                
                top = 0
                if i - 1 >= 0:
                    top = grid[i-1][j]
                
                # print(grid[i][j])
                grid[i][j] = max(grid[i][j], left + top)
            
                
        # print(grid)
        return grid[m-1][n-1]
                
                
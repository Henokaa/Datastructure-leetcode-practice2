class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0]]
        inbound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        memo = {}
        
        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            # if not inbound(x,y):
            #     return float('inf')
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return grid[len(grid) - 1][len(grid[0]) - 1]
            
            left = float('inf')
            down = float('inf')
            if inbound(x+1, y):
                left = dfs(x + 1, y)
            if inbound(x, y + 1):
                down = dfs(x, y + 1)
            # print(x,y)
            res = min(left, down) + grid[x][y]
            memo[(x,y)] = res
            return memo[(x,y)]
        
        
        return dfs(0,0)
                
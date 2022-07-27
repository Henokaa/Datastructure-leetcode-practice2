class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        row = len(grid)
        cols = len(grid[0])
        ans = []
        self.temp = 1
        value = 0
        maxanswer = 0
        def dfs(i,j):
            visited.add((i,j))
            for x,y in directions:
                a = i + x
                b = j + y
                if 0 <= a < row and 0<= b < cols and grid[a][b] == 1 and (a,b) not in visited:
                    self.temp += 1
                    visited.add((a,b))
                    dfs(a,b)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])): # i keep forgetting
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    value +=1
                    maxanswer = max(maxanswer, self.temp)
                    self.temp = 1
        
        return maxanswer
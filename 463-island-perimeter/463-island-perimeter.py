class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        inbound = lambda r,c: 0<= r <=len(grid)-1 and 0<= c <=len(grid[0])-1
        self.param = 0
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in directions:
                row = i + x
                cols = j + y
                if not inbound(row,cols) or grid[row][cols] == 0:
                    self.param += 1
                if inbound(row,cols) and grid[row][cols] == 1:
                    dfs(row,cols)
                    
                    
                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    dfs(i,j)
                    break
                    
        return self.param
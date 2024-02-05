class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        self.count = 0
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in directions:
                if not inbound(i + x, j + y) or grid[i+x][j+y] == 0:
                    self.count += 1
                if (i+x,j+y) not in visited and inbound(i+x,j+y) and grid[x+i][y+j] == 1:  
                    # visited.add((i+x,j+y))
                    dfs(i+x,j+y)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    
            
        return self.count
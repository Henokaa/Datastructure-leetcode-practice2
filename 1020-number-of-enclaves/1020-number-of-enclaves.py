class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.count = 0
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        inbound = lambda r,c: 0<= r <len(grid) and 0<= c <len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count += 1
                    
        def dfs(i,j):
            if (i,j) in visited:
                 return 
            
            self.count -= 1
            visited.add((i,j))
            for x,y in directions:
                dx = i + x
                dy = j + y
                if inbound(dx,dy) and grid[dx][dy] == 1 and (dx, dy) not in visited:
                    dfs(dx,dy)
          
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                dfs(0,i)
            if grid[len(grid) - 1][i] == 1:
                dfs(len(grid)-1, i)
        
        for j in range(len(grid)):

            if grid[j][0] == 1:
                dfs(j,0)
            if grid[j][len(grid[0]) - 1] == 1:  # this got me bad
                dfs(j, len(grid[0]) - 1)
        print(visited)
        return self.count
        
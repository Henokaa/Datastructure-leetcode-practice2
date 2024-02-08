class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        cover row and cols
        do dfs(1) save in visted
        '''
        visited = set()
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x, y in directions:
                dr = i + x
                dc = j + y
                if inbound(dr,dc) and grid[dr][dc] == 1:
                    dfs(dr,dc)
            
        visited = set()
        
        for r in range(len(grid)):
            if grid[r][0] == 1:
                if (r,0) not in visited:
                    dfs(r,0)
                
            if grid[r][len(grid[0])-1] == 1:
                if (r,len(grid[0])-1) not in visited:
                    dfs(r, len(grid[0])-1)
                
                
                
        for c in range(len(grid[0])):
            if grid[0][c] == 1:
                if (0,c) not in visited:
                    dfs(0,c)
            
            if grid[len(grid)-1][c] == 1:
                if (len(grid)-1,c) not in visited:
                    dfs(len(grid)-1,c)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count += 1
                    
        return count
                    
            
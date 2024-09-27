class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = []
        
        # grid = [['.'] * n for i in range(m)]
        
        for i in range(m):
            grid.append(['.'] * n)
        
        for x,y in guards:
            grid[x][y] = "G"
        
        for x,y in walls:
            grid[x][y] = "W"
        
        for i in range(len(grid)):
            guard = False
            
            for j in range(len(grid[0])):
                if grid[i][j] == "G":
                    guard = True
                
                elif grid[i][j] == "W":
                    guard = False
                elif guard:
                    grid[i][j] = "X"
                
        

        for i in range(len(grid)-1, -1, -1):
            guard = False
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == "G":
                    guard = True
                elif grid[i][j] == "W":
                    guard = False
                elif guard:
                    grid[i][j] = "X"
        
        
        for i in range(len(grid[0])):
            guard = False
            for j in range(len(grid)):
                if grid[j][i] == "G":
                    guard = True
                
                elif grid[j][i] == "W":
                    guard = False
                
                elif guard:
                    grid[j][i] = "X"
                    
        for i in range(len(grid[0]) - 1, -1, -1):
            guard = False
            for j in range(len(grid)-1, -1, -1):
                if grid[j][i] == "G":
                    guard = True
                
                elif grid[j][i] == "W":
                    guard = False
                
                elif guard:
                    grid[j][i] = "X"
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    count += 1
        
        return count
                
        
        
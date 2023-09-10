class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange = 0 
        rotten = collections.deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        time = 0
        inbound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    orange += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    
        while rotten and orange > 0:
            length = len(rotten) 
            for _ in range(length):
                x,y = rotten.popleft()
                for i, j in directions:
                    xi = i + x
                    yj = j + y
                    if inbound(xi,yj) and grid[xi][yj] == 1:
                        grid[xi][yj] = 2
                        orange -= 1
                        rotten.append((xi,yj))
            time += 1
            
        if orange == 0:
            return time
        return -1
            
            
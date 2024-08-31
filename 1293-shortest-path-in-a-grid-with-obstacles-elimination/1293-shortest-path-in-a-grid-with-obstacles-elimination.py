class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        bfs(obstacle , x , y )
        visited (x,y, obstacle)
        Time - (n * m) * k
        Space - (n * m) * k
        '''
        block = 0
        directions = [[0,1], [1,0], [0, -1], [-1, 0]]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        # check if grid is valid
        
        if grid[0][0] == 1:
            block += 1
        
        visited = set()
        que = deque()
        que.append((block, 0, 0, 0))
        visited.add((block, 0, 0, 0))
        
        while que:
            block, x, y, level = que.popleft()
            
            if x == len(grid)-1 and y == len(grid[0]) - 1:
                return level
            
            for x1, y1 in directions:
                nx = x1 + x
                ny = y1 + y

                new_block = block
                if inbound(nx, ny) and grid[nx][ny] == 1:
                    new_block += 1
                
                if (new_block, nx, ny) in visited:
                    continue
                
                if new_block > k:
                    continue
                
                if inbound(nx, ny): 
                    que.append((new_block, nx, ny, level + 1))
                    visited.add((new_block, nx, ny))
        
        return -1
                
                
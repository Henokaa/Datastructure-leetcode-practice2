class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        '''
        dijkstra (blocks, x, y,)
        visited (x, y, blocks)
        Time complexity - (m * n)log(m * n)
        Space  - (m * n)
        '''
        
        que = []
        block = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        if grid[0][0] == 1:
            block += 1
        
        visited = {}
        
        heapq.heappush(que, (block, 0, 0, 0))
        
        while que:
            block, x, y, level = heapq.heappop(que)
            
            # print(block, x, y)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return block
            
            for x1,y1 in directions:
                nx = x1 + x
                ny = y1 + y
                
                new_block = block
                if inbound(nx,ny) and grid[nx][ny] == 1:
                    new_block += 1
                    
                if (nx,ny) in visited and visited[(nx,ny)] <= new_block:
                    continue
                    
                if inbound(nx,ny) and (nx,ny,new_block) not in visited:
                    heapq.heappush(que, (new_block, nx, ny, level + 1))
                    visited[(nx, ny)] = new_block
                
        return -1
                
                
            
            
        
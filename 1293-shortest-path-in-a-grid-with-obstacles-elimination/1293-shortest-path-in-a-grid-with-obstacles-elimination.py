class Solution:
    def shortestPath(self, grid: List[List[int]], kmax: int) -> int:
        # bfs
        R = len(grid)
        C = len(grid[0])
        
        best = {}
        q = []
        nk = 0
        if grid[0][0] == 1:
            nk += 1
        
        best[(0,0,nk)] = 0 
        heapq.heappush(q, (0,0,0, nk))
        directions = [(-1,0), (0,-1), (1,0), (0, 1)]
        
        while len(q) > 0:
            # print(q)
            steps, x, y, k = heapq.heappop(q)
            
            if x == R - 1 and y == C - 1:
                return steps
            
            # if best[(x,y,k)] > steps:
            #     continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < R and 0 <= ny < C:
                    nk = k
                    
                    if grid[nx][ny] == 1:
                        nk += 1
                        
                    if nk > kmax:
                        continue
                        
                    key = (nx, ny, nk)
                    if key not in best:
                        best[key] = steps + 1
                        heapq.heappush(q, (steps + 1, nx, ny, nk))
                                          
        return -1
            
        
        
        
        
        
        
                                       
                                       
                        
                        
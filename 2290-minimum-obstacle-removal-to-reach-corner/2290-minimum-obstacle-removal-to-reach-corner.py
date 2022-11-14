class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # que bfs
        R = len(grid)
        C = len(grid[0])
        
        INF = 10 ** 20
        
        h = []
        heapq.heappush(h, (0,0,0))
        distances = {}
        distances[(0,0)] = 0
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        while len(h) > 0:
            d,x,y = heapq.heappop(h)
            
            if d > distances[(x,y)]:
                continue
            if x == R-1 and y == C-1:
                return d
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0<= nx < R and 0 <= ny < C:
                    nd = d
                    
                    if grid[nx][ny] == 1:
                        nd += 1
                    if (nx,ny) not in distances or distances[(nx,ny)] > nd:
                        distances[(nx,ny)] = nd
                        heapq.heappush(h, (nd, nx, ny))
                        
#         return distances[R - 1][C - 1]
        
                
        
        
        
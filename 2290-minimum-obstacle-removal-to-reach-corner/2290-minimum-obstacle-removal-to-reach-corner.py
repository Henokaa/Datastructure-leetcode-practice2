class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        '''
        visited((nr,nc)) = k is a must otherwise TLE, i think optimization technqiue 
        time-complexity - E*logE
        space-complexity - 0(E)
        '''
        # que bfs
        que = []
        visited = {}
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0])
        k = 0
        if grid[0][0] == 1:
            k += 1
        heapq.heappush(que, (k,0,0))
        visited[(0,0)] = k
        while que:
            k, x, y = heapq.heappop(que)
            
            if visited[(x,y)] < k:
                continue
                
            if x == len(grid)-1 and y == len(grid[0])-1:
                return k
            
            
                
            for r, c in directions:
                nr = x + r
                nc = y + c
                
                if inbound(nr,nc):
                    nk = k
                    if grid[nr][nc] == 1:
                        nk += 1
                    if (nr,nc) not in visited or visited[(nr,nc)] > nk:
                        heapq.heappush(que, (nk,nr,nc))
                        visited[(nr,nc)] = nk
                
        
                
        
        
        
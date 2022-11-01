class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs
        que = deque()
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0])
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1]:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
            return 0
            
        que.append((0,0,0))
        visited.add((0,0, 0))
        level = 0
        while que:
            length = len(que)
            for i in range(length):
                a, b, blocks = que.popleft()
                if a == len(grid)-1 and b == len(grid[0])-1:
                        return level
                for x,y in directions:
                    dr = a + x
                    dc = b + y
                
                    if inbound(dr,dc) and (dr,dc, blocks + 1) not in visited and grid[dr][dc] == 1 and blocks + 1 <= k:
                        que.append((dr,dc, blocks + 1))
                        visited.add((dr,dc, blocks + 1))
                    elif inbound(dr,dc) and (dr,dc, blocks) not in visited and grid[dr][dc] == 0:
                        que.append((dr,dc, blocks))
                        visited.add((dr,dc, blocks))
                    
            level += 1
            
        return -1
            
                        
                        
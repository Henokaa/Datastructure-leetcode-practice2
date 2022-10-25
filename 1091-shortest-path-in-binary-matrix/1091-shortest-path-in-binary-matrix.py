class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        bfs 
        
        '''
        
        # declare our direction
        directions = [[0,1],[1,0],[-1, 0], [0, -1],[1,1], [-1,-1],[-1,1],[1,-1]]
        inbound = lambda r, c: 0<=r<len(grid) and 0 <= c<len(grid[0])
        # que
        que = deque()
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        if grid[0][0] == 0:
            que.append((0,0))
        else:
            return -1
    
        visited = set()
        visited.add((0,0))
        level = 1
        # bfs 
        
        while que:
            # print(que)
            length = len(que)
            for i in range(length):
                temp1 = que.popleft()
                for x,y in directions:
                    dr = temp1[0] + x
                    dc = temp1[1] + y
                    if inbound(dr,dc) and (dr,dc) not in visited and grid[dr][dc] == 0:
                        
                        if (dr,dc) == (len(grid)-1,len(grid[0])-1):
                            return level + 1
                        que.append((dr,dc))
                        visited.add((dr,dc))
            
            level += 1
        return -1
                
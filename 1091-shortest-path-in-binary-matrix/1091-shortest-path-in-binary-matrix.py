class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        bfs
        '''
        #
        directions = [(0,1), (1,0), (-1,0), (0, -1), (1,1), (1,-1), (-1, 1), (-1,-1)]
        inbound = lambda x,y: 0<= x < len(grid) and 0<= y < len(grid[0])
            
        if grid[0][0] == 1:
            return -1
        
        que = deque()
        visited = set()
        que.append((0,0))
        visited.add((0,0))
        level = 0
        while que:
            length = len(que)
            for _ in range(length):
                i,j = que.popleft()

                if len(grid) - 1 == i and len(grid[0]) - 1 == j and grid[i][j] == 0:
                    return level + 1

                for x,y in directions:
                    x_1 = x + i
                    y_1 = y + j

                    if (x_1, y_1) not in visited and inbound(x_1, y_1) and grid[x_1][y_1] == 0:
                        que.append((x_1, y_1))
                        visited.add((x_1, y_1))

            level += 1
        
        return -1
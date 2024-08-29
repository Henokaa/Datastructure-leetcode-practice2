class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        node
        bfs
        que(x,y, level)
        8 direct
        '''
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) 
        que = deque()
        if not grid[0][0] == 0:
            return -1
        visited = set()
        que.append((0,0,0))
        visited.add((0,0))
        while que:
            x,y, level = que.popleft()
            # print((x,y))
            if x == len(grid)-1 and y == len(grid[0])-1:
                return level +1
            
            for x_1, y_1 in directions:
                if inbound(x+x_1, y+y_1) and grid[x+x_1][y+y_1] == 0:
                    if (x +x_1, y+y_1) in visited:
                        continue
                    que.append((x+x_1, y+y_1, level + 1))
                    visited.add((x+x_1, y+y_1))
        
        return -1
            
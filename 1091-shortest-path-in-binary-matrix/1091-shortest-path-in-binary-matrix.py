class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        que = deque()
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1,1),(-1,-1),(1,1),(1,-1)]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        visited = set()
        if grid[0][0] != 0:
            return -1
        
        if grid[0][0] == 0 and 0 == len(grid)-1 and 0 == len(grid[0]) - 1:
            return 1
        
        que.append((0,0))
        
        level = 1
        while que:
            length = len(que)
            # print(que, level)
            for i in range(length):
                position = que.popleft()
                for x,y in directions:
                    x1 = position[0] + x
                    y1 = position[1] + y
                    
                    if x1 == len(grid) - 1 and y1 == len(grid[0]) - 1 and grid[x1][y1] == 0:
                        # print("A",(x1, y1), (position))
                        return level + 1
                    
                    if inbound(x1,y1) and (x1,y1) not in visited and grid[x1][y1] == 0:
                        visited.add((x1,y1))
                        que.append((x1,y1))
            
            level += 1
        
        return -1
                    
                
            
            
            
                
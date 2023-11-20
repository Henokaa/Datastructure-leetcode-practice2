class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        visited = set()
        temp = set()
        que = deque()
        self.area = 0
        maxarea = 0
        def bfs(i,j):
            while que:
                length = len(que)
                for _ in range(length):
                    cx, cy = que.popleft()
                    self.area += 1
                    for x,y in directions:
                        if inbound(cx + x,cy + y) and grid[cx + x][cy + y] == 1 and (cx + x, cy + y) not in visited:
                            que.append((cx + x, cy + y))

                            visited.add((cx + x, cy + y))

                    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    que = deque()
                    que.append((i,j))
                    bfs(i,j)
                    maxarea = max(maxarea, self.area)
                    self.area = 0
                
                    
                    
        return maxarea
                    
    
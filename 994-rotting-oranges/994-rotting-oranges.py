class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = []
        self.ans = 0
        self.fresh = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot.append((i,j))
                if grid[i][j] == 1:
                    self.fresh += 1
        
        
        def bfs():
            q = collections.deque()
            for x,y in rot:
                q.append((x,y))
            while q and self.fresh >0:
                for w in range(len(q)):
                    a,b =q.popleft()
                    for x,y in directions:
                        r = a + x
                        c = b + y
                        if 0<= r < len(grid) and 0<= c < len(grid[0]) and grid[r][c] == 1:
                            self.fresh -= 1
                            grid[r][c] = 2
                            q.append((r,c))
                self.ans += 1
                
                    
        bfs()
        print(self.fresh)
        return self.ans if self.fresh == 0 else -1
    
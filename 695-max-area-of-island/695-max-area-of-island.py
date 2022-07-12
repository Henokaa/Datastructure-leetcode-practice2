class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        parent = {}
        rank = {}
        direction = [[1,0], [0, 1], [-1, 0], [0, -1]]
        inbound = lambda r, c: 0<= r <len(grid) and 0<= c <len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    parent[(i,j)] = (i, j)
                    rank[(i,j)] = 1
        
        def findset(x):
            if x == parent[x]:
                return x
            # parent[x] = findset(parent[x])
            return findset(parent[x])
        
        def union(x,y):
            x = findset(x)
            y = findset(y)
            
            if x != y:
                parent[x] = y
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for r, c in direction:
                        nr, nc = i + r, j + c
                        if inbound(nr, nc) and grid[nr][nc] == 1:
                            union((i,j), (nr,nc))
        
        count = {}
        maxcount = 0
        for i in parent.keys():
            x = findset(i)
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
                
            maxcount = max(maxcount, count[x])
        return maxcount
                
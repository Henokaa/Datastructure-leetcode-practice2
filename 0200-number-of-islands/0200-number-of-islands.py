class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        count = 0
        parent = [-1 for i in range(row*cols)]
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda r,c: 0<= r < len(grid) and 0<= c < len(grid[0])
        
        def find(node):
            if parent[node] < 0:
                return node
            
            root = find(parent[node])
            parent[node] = root
            return root
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return
            
            if abs(parent[root1]) >= abs(parent[root2]):
                parent[root1] += parent[root2]
                parent[root2] = root1
            
            else:
                parent[root2] += parent[root1]
                parent[root1] = root2
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    
                    for x, y in directions:
                        nr = i + x
                        nc = j + y
                        if inbound(nr,nc) and grid[nr][nc] == "1":
                            union(i*cols + j, nr*cols + nc)
                    
         
        for x in range(len(parent)):
            r = x // cols
            c = x % cols
            if grid[r][c] == "1" and parent[x] < 0:
                count += 1
        return count
                            
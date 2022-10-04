class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        if the grid in grid2 then it must be in grid1
                    grid1 not in grid2 - okay

        '''
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        inbound = lambda r,c: 0<=r<len(grid1) and 0<=c<len(grid1[0])
        # dfs 
        # if grid2[i][j] == 1 and not grid1[i][j] == 1 and not in visited
        #   break
        def dfs(i, j):
            if (i,j) in visited2:
                return
            visited2.add((i,j))
            for dr, dc in directions:
                row = i + dr
                cols = j + dc
                if inbound(row, cols) and grid2[row][cols] == 1 and grid1[row][cols] == 0:
                   
                    self.flag = 1
                if inbound(row,cols) and grid1[row][cols] == 1 and grid2[row][cols] == 1 and (row,cols) not in visited2:
                    dfs(row,cols)
            



        # traverse to both grid1 and grid2
        visited2 = set()
        subIslands = 0
        self.flag = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1 and grid2[i][j] == 1 and (i,j) not in visited2:
                    self.flag = 0
                    dfs(i,j)
                    if self.flag == 0:
                        subIslands += 1
                
                
        return subIslands
                

                
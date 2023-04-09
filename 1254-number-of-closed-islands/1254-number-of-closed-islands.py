class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        count = 0
        
        
        def dfs(i, j):
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    self.is_closed = False
                
                elif grid[x][y] == 0 and (x, y) not in visited:
                    dfs(x, y)
                else:
                    visited.add((x, y))
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 0:
                    self.is_closed = True
                    dfs(i, j)
                    if self.is_closed == True:
                        count += 1

        return count
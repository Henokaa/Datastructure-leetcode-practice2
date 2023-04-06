class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        count = 0

        def dfs(i, j):
            visited.add((i, j))
            is_closed = True

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                    is_closed = False
                elif grid[x][y] == 0 and (x, y) not in visited:
                    if not dfs(x, y):
                        is_closed = False
                else:
                    visited.add((x, y))

            return is_closed

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count
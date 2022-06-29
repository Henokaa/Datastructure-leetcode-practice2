class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        row = len(board)
        cols = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        # ans = [[]]*3
        # print(ans)
        
        def dfs(i,j):
            visited.add((i,j))
            for x, y in directions:
                a = i + x
                b = j + y
                if 0<= a < row and 0<= b < cols and board[a][b] == "O" and (a,b) not in visited:
                    visited.add((a,b))
                    dfs(a,b)
                
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
                
        for c in range(len(board[0])):
            if board[0][c] == "O":
                dfs(0,c)
            if board[row-1][c] == "O":
                dfs(row-1,c)
        print(visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited:
                    board[i][j] = "X"
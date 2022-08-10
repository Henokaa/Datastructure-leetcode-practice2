class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x = click[0]
        y = click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
        inbound = lambda r,c :0<= r<len(board) and 0<= c <len(board[0]) # puting , instead of and
        
        def dfs(x,y):
            if board[x][y] != "E":
                return
            count = 0
            for dr, dc in directions:
                dx = x + dr
                dy = y + dc
                if inbound(dx,dy) and board[dx][dy] == "M":
                    count += 1     
            
            
            if count > 0:
                board[x][y] = str(count)
                return
            else:
                board[x][y] = "B"
                
            
            for dr, dc in directions:
                dx = x + dr
                dy = y + dc
                if inbound(dx,dy) and board[dx][dy] == "E":
                    dfs(dx, dy)
        
        dfs(x,y)
        return board
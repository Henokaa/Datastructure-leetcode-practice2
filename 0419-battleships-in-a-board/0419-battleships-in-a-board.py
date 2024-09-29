class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''
        
        time - o(2n)
        space - (n * m)
        
        '''
        visited = set()
        count =0
        directions = [[0,1], [1,0], [-1,0],[0,-1]]
        
        inbound = lambda x, y: 0 <= x < len(board) and 0 <= y < len(board[0])
        
        def dfs(i, j):
            # visited.add((i,j))
            for x,y in directions:
                x1 = x + i
                y1 = y + j
                
                if inbound(x1, y1) and board[x1][y1] == "X" and (x1, y1) not in visited:
                    visited.add((x1, y1))
                    dfs(x1, y1)
                    
                    
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == "X":
                    dfs(i,j)
                    count += 1
                    visited.add((i,j))
        
        return count
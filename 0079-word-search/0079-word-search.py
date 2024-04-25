class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        
        '''
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        inbound = lambda x, y: 0 <= x < len(board) and 0 <= y < len(board[0])
        def dfs(i,j,k):
            if k == len(word):
                return True
            
            # print(k)
            node = False
            for x,y in directions:
                dr = x + i
                dc = y + j
                if inbound(dr,dc) and board[dr][dc] == word[k] and (dr,dc) not in visited:
                    visited.add((i,j))
                    node =  dfs(dr,dc,k+1)
                    if node == True:
                        return True
                    visited.remove((i,j))
            
            return False
                
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if dfs(i,j, 1):
                        return True
                    
        return False
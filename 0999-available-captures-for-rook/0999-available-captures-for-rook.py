class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        
        '''
        inbound = lambda x,y: 0 <= x < len(board) and 0 <= y < len(board[0])
        self.count = 0
        def dfs(i,j):
            
            for x in range(1, len(board[0])):
                if inbound(i, j + x):
                    if board[i][j+x] == 'p':
                        self.count += 1
                        break
                    if board[i][j+x] == 'B':
                        break
                else:
                    print("B", (i,j+x))
                    break
            
            for x in range(1, len(board[0])):
                if inbound(i, j - x):
                    if board[i][j- x] == 'p':
                        self.count += 1
                        break
                    if board[i][j- x] == 'B':
                        break
                else:
                    break
            # print(self.count)
            for y in range(1, len(board)):
                if inbound(i + y, j):
                    if board[i+y][j] == 'p':
                        self.count += 1
                        break
                    if board[i+y][j] == 'B':
                        break
                else:
                    break
            
            
            for y in range(1, len(board)):
                if inbound(i - y, j):
                    if board[i-y][j] == 'p':
                        self.count += 1
                        break
                    if board[i-y][j] == 'B':
                        break
                else:
                    break
            
            
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    # print((i,j), board[i][j])
                    dfs(i,j)
                    break
        
       
        return self.count
        
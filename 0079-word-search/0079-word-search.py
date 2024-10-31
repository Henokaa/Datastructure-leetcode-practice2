class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        
        constraint
        
        naive
        
        optimal
        
        edge case

        [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
         
        Time - 0 (N * M * 4 ^ len(word))
        Search pruning
        count the character board & word
            check
        
        dfs()
            assigning = "#"
            
            for
            
            orgina
        '''
        
        word_board = defaultdict(int)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                word_board[board[i][j]] += 1
        
        # print(word_board)
        
        word_count = Counter(word)
        # print(word_count)
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for char, val in word_count.items():
            if char in word_board and word_board[char] >= word_count[char]:
                continue
            else:
                return False
            
        def dfs(i,j, index):
            if index == len(word) - 1:
                return True
            
            orginal = board[i][j]
            board[i][j] = "#"
            
            for x,y in directions:
                x1 = x + i 
                y1 = y + j
                if 0<= x1 < len(board) and 0<= y1 < len(board[0]) and board[x1][y1] == word[index+1]:
                    node = dfs(x1,y1, index + 1)
                    if node:
                        return True
            
            board[i][j] = orginal
            return False
                    
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    node = dfs(i,j,0)
                    if node:
                        return True
        
        return False
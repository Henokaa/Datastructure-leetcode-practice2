class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                    if j > 0 and board[i][j-1] == 'X':
                        continue
                    count += 1
        return count
                        
        # horizontal
        # n + 1
        # it should be the start
        
        # vertical
        # one down
        # it should be the start
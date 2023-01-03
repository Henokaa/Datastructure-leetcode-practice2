class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in row[i]:
                        return False
                    row[i].add(board[i][j])
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])
                    if board[i][j] in box[(i//3, j//3)]:
                        return False
                    box[(i//3, j//3)].add(board[i][j])
        return True
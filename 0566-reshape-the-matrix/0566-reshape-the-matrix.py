class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        '''
        
        num = 3
        
        
        
        '''
        grid = [[0] * c for _ in range(r)]
        row = len(mat)
        cols = len(mat[0])
        if r * c != row * cols:
            return mat
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                item = i * len(mat[0]) + j
                grid[item // len(grid[0])][item % len(grid[0])] = mat[i][j]
        
        return grid
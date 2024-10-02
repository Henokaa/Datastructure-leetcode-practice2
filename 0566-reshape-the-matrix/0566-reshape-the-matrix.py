class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        '''
        
        num = 3
        
        
        Just playing around
        '''
        grid = [[0] * c for _ in range(r)]
        
        if r * c != len(mat[0]) * len(mat):
            return mat
        
        for i in range(r):
            for j in range(c):
                number = (i * c) + j # I get this wrong it is (i * c) not i * r
                
                
                row = number // len(mat[0])
                cols = number % len(mat[0])
                # print(grid[i][j], (i,j), (row, cols))
                
                grid[i][j] = mat[row][cols]
            
        return grid
                
                
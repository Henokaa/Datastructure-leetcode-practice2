class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        edge
        
        naive
        
        optimal
        
        '''
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            
        for i in range(len(matrix)):
            temp = matrix[i][::-1]
            matrix[i] = temp
            
                
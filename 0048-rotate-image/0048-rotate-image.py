class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Time Complexity: O(N²), where N is the number of rows/columns.
        Space Complexity: O(1) (in-place solution).     
        '''
        n = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()        
        
        
        
                
                
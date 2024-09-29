class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        last 
            horizontally
            we assign to the column
            
            vertically <= assigned
            
        (3, 0) => (0,0)
        (3,1) +> (1,0)
        3,2) => (2,0)
        
        temp_y = 0
        for i in range(len(matrix)-1, -1, -1):
            
            for j in range(len(matrix[0])):
                matrix[j][temp_y] = matrix[i][j]
            print(matrix)
            temp_y += 1
            
        [[7, 2, 3], 
        [8, 5, 6], 
        [9, 8, 9]]
        
        
    
        '''
        n = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()        
        
        
        
                
                
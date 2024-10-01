class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top = l
                bottom = r
                
                # pick top right
                top_right = matrix[top + i][r]
                
                # put TL -> TR
                matrix[top + i][r] = matrix[top][l + i]
                
                # pick bottom right
                bottom_right = matrix[bottom][r - i]
                
                # put TR -> BR
                matrix[bottom][r - i] = top_right
                
                # pick bottom left
                bottom_left = matrix[bottom - i][l]
                
                # put BR -> BL
                matrix[bottom - i][l] = bottom_right
                
                # pick TL
                TL = matrix[top][l + i]
                
                # put Bottom left -> Top left
                matrix[top][l + i] = bottom_left
            
            l += 1
            r -= 1
                
                
        
        
                
                
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90(mat):
            n = len(mat)
            # Transpose the matrix
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # Reverse each row
            for i in range(n):
                mat[i].reverse()
        
        for _ in range(4):
            if mat == target:
                return True
            rotate90(mat)  # Rotate mat by 90 degrees
        return False
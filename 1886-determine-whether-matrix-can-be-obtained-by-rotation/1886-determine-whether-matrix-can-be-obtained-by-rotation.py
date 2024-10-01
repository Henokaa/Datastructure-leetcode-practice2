class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rot(matrix):
            N = len(matrix)
            
            nmatrix = [[0] * N for _ in range(N)]
            
            for x in range(N):
                for y in range(N):
                    nmatrix[x][y] = matrix[N - y - 1][x]
            
            return nmatrix
        
        def eq(m1, m2):
            N = len(m1)
            
            for x in range(N):
                for y in range(N):
                    if m1[x][y] != m2[x][y]:
                        return False
                    
            return True
        
        current = mat
        if eq(current, target):
            return True
        
        for _ in range(4):
            current = rot(current)
            if eq(current, target):
                return True
            
        return False
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        A = matrix
        N = len(A)
        M = len(A[0])
        
        res = [[0] * N for _ in range(M)]
        
        print(res)
        for i in range(M):
            for j in range(N):
                res[i][j] = A[j][i]
        return res
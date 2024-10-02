class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        '''
        check
        
        when n
        '''
        grid = [[0] * n for _ in range(m)]
        
        if m * n != len(original):
            return []
        print(grid)
        for i in range(m):
            for j in range(n):
                number = (i * n) + j
                
                
                grid[i][j] = original[number]
                
        return grid
                
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        '''
        
        '''
        nums = mat
        rows = len(nums)
        cols = len(nums[0])

        if rows * cols != r * c:  # Check if sizes match
            return nums

        reshaped = [[0] * c for _ in range(r)]  # Initialize reshaped matrix
        # print("Row", (rows, cols))
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                # print(index,i,j)
                reshaped[index // c][index % c] = nums[i][j]

        return reshaped

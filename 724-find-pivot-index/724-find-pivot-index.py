class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        [1, 7, 3, 6, 5, 6]
         0  1  8  11 17 22
         
        22  21 14 11  6  0
S - 28
leftSum - 
        '''
        S = sum(nums)
        print(S)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1, 2, 3, 4]
        [1, 1, 2, 6]
        [24, 12, 8, 6]
        
  pre =[1,2, 6, 24]
      =[1, 1, 2, 6]
  post=[24 , 24, 12,4]
        
        '''
        
        res = [1] * len(nums)
        for i in range(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        print(res)
        tmp = 1
        for i in range(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        print(res)
        return res
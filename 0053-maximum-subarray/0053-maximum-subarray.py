class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
                           ^
                ^
        
        [-2,1,-3,4,-1,2,1,-5,4]
                    ^
               ^  
        left - sum 0, l =r , add r, 
        '''
        
        r = 0
        prefix = 0
        mx = float('-INF')
        while r < len(nums):
            prefix += nums[r]
            mx = max(mx, prefix)
            if prefix < 0:
                prefix = 0
            
            r += 1
        
        return mx
            
        
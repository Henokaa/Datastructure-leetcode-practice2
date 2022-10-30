class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
                           ^
        [-2,-1,-4,0,-1,1,2,-3,1]
                  ^
        
        [-2,1,-3,4,-1,2,1,-5,4]
                    ^
               ^  
        [5,4,-1,7,8]
        [5,9,8,15,23]
        
        '''
        
        r = 0
        total = 0
        mn = float('inf')
        ans = float('-inf')
        while r < len(nums):
            total += nums[r]
            if r >= 1:
                mn = min(mn, total - nums[r])
            ans = max(ans, total - mn, total)
            r += 1
        return ans
        
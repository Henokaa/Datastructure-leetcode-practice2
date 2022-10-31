class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        [1,1,1,0,0,1,1,1,1,0]               k = 2
        [1,2,3,0,0,1,2,3,4,0]
        [3,2,1,0,0,4,3,2,1,0]
        
        
        [1,1,1,0,0,0,1,1,1,1,0]
                   ^
        ^
        '''
        
        l = 0
        r = 0
        zeros = 0
        mx = 0
        while r < len(nums):
            # the statement first then check, my weakness
            if nums[r] == 0:
                zeros += 1
                
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1 
                
            if zeros <= k:
                mx = max(mx, r - l + 1)
                r += 1
             
        return mx
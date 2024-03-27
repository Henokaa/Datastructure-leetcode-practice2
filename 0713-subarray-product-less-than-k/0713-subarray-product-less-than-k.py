class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        [10,5,2,6]
            ^
              ^
        k = 100
        
        
        '''
        l = 0
        r = 0
        total = 1
        count = 0
        while r < len(nums):
            total = total * nums[r]
            while total >= k and l <= r:
                total = total // nums[l]
                l += 1
                
            if total < k:
                # print(l,r)
                count += r - l + 1
            r += 1
            
        return count
            
                
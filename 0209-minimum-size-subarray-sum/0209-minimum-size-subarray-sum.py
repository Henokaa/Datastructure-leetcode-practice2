class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        
        prefix sum
            check if total - target in set
            
            
        '''
        
        l = 0
        r = 0
        total = 0
        length = float(inf)
        while r < len(nums):
            total += nums[r]
            
            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
                
            
        return length if length != float(inf) else 0
        
                
                
            
                
        
                
                
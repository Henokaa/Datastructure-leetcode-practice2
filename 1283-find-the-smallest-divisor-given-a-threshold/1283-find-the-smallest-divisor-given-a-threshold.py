class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        [1,2,5,9]
         1 = 17
         4 = 7
         5 = 5
         
         
        1 - 9
        
        '''
        l = 0
        r = max(nums) + 1
        while r > l + 1:
            mid = l + (r - l)//2
            ans = 0
            for x in nums:
                ans += ceil(x/mid)
                
            if ans > threshold:
                l = mid
            else:
                r = mid
                
        return r
                
                
            
        
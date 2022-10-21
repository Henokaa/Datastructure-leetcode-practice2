class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        in sliding window because it have a negative when we remove the first index it doesn't mean we will decrease the size
        [1, 1, 1]    k = 2
        [1 , -1, 1, -1]  k = 0
         1    0  1   0
        
        
           [1, 2, 3]   k = 3
        
        [0, 1, 3, 6]
        
        if prefixsum == 3 what we want is prefix of 0        
        prefixsum - k = the prefix we want
        
        '''
        r = 0
        total = 0
        prefix = {}
        prefix[0] = 1
        answer = 0
        while r < len(nums):
            total += nums[r]
            if (total - k) in prefix:
                answer += prefix[total - k]
                
            if total in prefix:
                prefix[total] += 1
            else:
                prefix[total] = 1
            
            r += 1
        
        return answer
            
            
        
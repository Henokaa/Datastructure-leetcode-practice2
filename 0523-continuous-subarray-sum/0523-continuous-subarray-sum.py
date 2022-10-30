class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        [23,2,4,6,7]
        
        [23,25,29,35,42]
        [5, 1, 5, 5, 0]
        
        [23,2,6,4,7]
        [23,25,31,35,42]
        
        '''
        prefix = []
        save = defaultdict(int)
        r = 0
        total = 0
        ans = 0
        while r < len(nums):
            total += nums[r]
            prefix.append(total)
            curr = total % k
            if len(prefix) >= 3:
                value = prefix[r-2]
                save[value%k] += 1
                
            
            if curr in save:
                ans += save[curr]
                return True
                
            if r >= 1 and curr == 0:
                ans += 1
                return True
            
            
            r += 1
        return False
     
        ''' do it with constant space'''
        
        
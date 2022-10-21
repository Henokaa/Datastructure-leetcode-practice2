class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        
        [1,4,8,13]     k = 5
             
        sort
        num[r] * len - total - will give as how many k we need and compare it with the k that we         have
        
        we are to make everything num[r] 
        and num[r] * len = the prefix sum that we need
        total - the prefix sum that we have

        '''
        nums = sorted(nums)
        r = 0
        l = 0
        mx = float('-inf')
        total = 0
        while r < len(nums):
            total += nums[r]
            # print(nums[r] * (r - l + 1) - total)
            while nums[r] * (r - l + 1) - total > k:
                total -= nums[l]
                l += 1
            mx = max(mx, r - l + 1)
            r += 1
        
        return mx
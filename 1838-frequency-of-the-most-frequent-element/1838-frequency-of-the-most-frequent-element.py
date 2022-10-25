class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        [1,4,8,13]  k = 5
         ^
           ^
         24, 13
         [1,5,13,26]
        '''
        # prefix
        nums = sorted(nums)
        total = 0
        pre = []
        for i in nums:
            total += i
            pre.append(total)
        
        # making our sliding window, return the max valid window length
        r = 1
        l = 0
        answer = 1
        while r < len(nums):
            window = r - l + 1
            needed = window*nums[r]
            if l - 1 >= 0:
                have = pre[r] - pre[l - 1]
            else:
                have = pre[r]
            total = needed - have
            if total <= k:
            
                answer = max(answer, window)
                r += 1
            elif total > k:
                l += 1
        return answer
            
            
            
        
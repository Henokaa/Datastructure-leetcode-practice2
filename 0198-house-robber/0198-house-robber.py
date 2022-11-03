class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums.insert(0,0)
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(nums[i] + dp(i+2), dp(i + 1))
            return memo[i]
            
            
            
        x =dp(0)
        
        return x
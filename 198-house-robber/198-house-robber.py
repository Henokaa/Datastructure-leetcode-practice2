class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            memo[i] = max(nums[i] + dp(i+2), dp(i+1))
            return memo[i]
        memo = {}
        return dp(0)
    
#     1,2,3,1
#     1,2,4,4
    
#     2,1,1,2
#     2,2,3,4
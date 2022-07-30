class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums) - 1]
    
#     1,2,3,1
#     1,2,4,4
    
#     2,1,1,2
#     2,2,3,4
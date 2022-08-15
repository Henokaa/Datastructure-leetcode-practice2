class Solution:
    def rob(self, nums: List[int]) -> int:
        
                # empty case
        if not nums:
            return 0
        
        dp = [None for x in range(len(nums)+1)]
        # base case
        dp[len(nums)] = 0
        dp[len(nums)-1] = nums[len(nums)-1]
        
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        
        return dp[0]
    
#     1,2,3,1
#     1,2,4,4
    
#     2,1,1,2
#     2,2,3,4
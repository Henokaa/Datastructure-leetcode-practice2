class Solution:
    def rob(self, nums: List[int]) -> int:
        temp = 0
        dp = []
        for i in range(len(nums)):
            if i < 2:
                temp = max(temp, nums[i])
                dp.append(temp)
                continue
            temp = 0
            temp = max(dp[i-2] + nums[i], dp[i-1])
            dp.append(temp)
        return dp[-1]
            
        
        
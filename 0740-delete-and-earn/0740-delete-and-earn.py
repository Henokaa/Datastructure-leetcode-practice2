class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        x = Counter(nums)
        # print(x)
        nums = sorted(list(set(nums)))
        # print(nums)
        
        dp = []
        for i in range(len(nums)):
            temp1 = 0
            temp2 = 0
            temp3 = 0
            val = 0
            if i-1 >= 0 and nums[i] - 1 != nums[i-1]:
                temp1 = dp[i-1]
            elif i - 2 >= 0:
                temp2 = dp[i-2]
            
            temp3 = max(temp1, temp2)
            if i-1 >=0:
                val = dp[i-1]
            dp.append(max(val, temp3 + (nums[i]*x[nums[i]])))
        return dp[-1]
            
            
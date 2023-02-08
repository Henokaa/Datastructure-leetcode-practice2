class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        saved = defaultdict(int)
        for i in nums:
            saved[i] += 1
        # print(saved)
        temp = list(set(nums))
        # print(temp)
        dp = []
        for i in range(len(temp)):
            val1 = 0
            val2 = 0
            ans = 0
            val1 = temp[i]*saved[temp[i]]
            if i-1 >= 0 and temp[i-1] == temp[i] - 1:
                if i - 2 >= 0:
                    val2 = dp[i-2]
                ans = max(dp[i-1] ,val1 + val2)
            else:
                if i - 1 >= 0:
                    val2 = dp[i-1]
                ans = val1 + val2
            dp.append(ans)
        return dp[-1]
            
        
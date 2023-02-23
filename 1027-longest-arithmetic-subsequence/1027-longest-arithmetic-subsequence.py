class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = collections.defaultdict(dict)
        result = 0
        N = len(nums)
        for i in range(N):
            dif_set = set()
            for j in range(i-1, -1, -1):
                dif = nums[i] - nums[j]
                
                if dif in dif_set: continue
                dif_set.add(dif)

                dp[i][dif] = dp[j].get(dif, 1) + 1
                result = max(result, dp[i][dif])
        
        return result
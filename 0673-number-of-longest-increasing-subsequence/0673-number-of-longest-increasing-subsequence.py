class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp, cnt = [0]*n, [1]*n
        max_len, ans = 1, 0
        def solve(i):
            nonlocal max_len
            if dp[i]: 
                return dp[i]
            max_val = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    val = solve(j)
                    if max_val == 1 + val:
                        cnt[i] += cnt[j]
                    elif max_val < 1 + val:
                        max_val = 1 + val
                        cnt[i] = cnt[j]
                        
            dp[i] = max_val
            
            max_len = max(max_len, max_val)
            
            return max_val
        
        for i in range(n):
            solve(i)
            # print(dp)
            # print(cnt)
            # print("------")
            
        return sum(c for l, c in zip(dp, cnt) if l == max_len)
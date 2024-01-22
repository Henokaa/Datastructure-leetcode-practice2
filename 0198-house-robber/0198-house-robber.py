class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}  # Memoization dictionary

        def dp(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 0

           
            rob_current = nums[i] + dp(i + 2)

            
            skip_current = dp(i + 1)

            # Store the maximum amount in the memoization dictionary
            memo[i] = max(rob_current, skip_current)

            return memo[i]
        left = dp(0)
        print(memo)
        return left

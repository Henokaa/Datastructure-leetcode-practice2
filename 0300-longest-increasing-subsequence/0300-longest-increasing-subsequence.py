class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def solve(idx):
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]
            
            maximum = 0
            compare = nums[idx]
            
            if idx == -1:
                compare = float('-inf')
                
            for i in range(idx + 1, len(nums)):
                if nums[i] > compare:
                    maximum = max(maximum, solve(i))
            memo[idx] = maximum + 1        
            return maximum + 1
        
        return solve(-1) - 1
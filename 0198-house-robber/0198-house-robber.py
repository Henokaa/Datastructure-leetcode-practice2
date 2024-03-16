class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1,2,3,1]
        
        max(i + dfs(i + 2), dfs(i + 1))
        '''
        memo = {}
        @cache
        def dfs(i):
            if i in memo:
                return 
            if i >= len(nums):
                return 0
            
            one = nums[i] + dfs(i + 2)
            two = dfs(i + 1)
            memo[i] = max(one, two)
            return max(one, two)
        
        return dfs(0)
        
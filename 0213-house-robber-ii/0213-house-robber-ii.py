class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        if it takes 0 = 1
        dfs(i,take_one)
        '''
        @cache
        def dfs(i, taken):
            # print(i, taken)
            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1 and taken == 1:
                return 0
            
            if i == 0:
                a = nums[i] + dfs(2, 1)
                b = dfs(i + 1,taken)
            else:
                a = nums[i] + dfs(i + 2,taken)
                b = dfs(i  + 1, taken)
            
            return max(a, b)
                
            
        return dfs(0, 0)
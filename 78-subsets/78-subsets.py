class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1, 2, 3]
        [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
        o(n * 2^n)
        8 choices with n elements max
        '''
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
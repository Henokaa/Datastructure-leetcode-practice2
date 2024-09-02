class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1, 2, 3]
        [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
        o(n * 2^n)
        space - height of a tree
        8 choices with n elements max
        '''
        
        ans = []
        def dfs(i, path):
            if i >= len(nums):
                ans.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path) 
            
        dfs(0, [])
        return ans
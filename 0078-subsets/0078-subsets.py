class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        [1, 2, 3]
        [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
        o(n * 2^n)
        space - height of a tree
        8 choices with n elements max
        '''
        
        def backtrack(i, path):
            if i > len(nums):
                return
            path.append(nums[i])
            ans.append(path.copy())
            for x in range(i + 1, len(nums)):
                backtrack(x, path)
                path.pop()  
                
                
        ans = []
        for i in range(len(nums)):
            backtrack(i, [])
        ans.append([])
        return ans
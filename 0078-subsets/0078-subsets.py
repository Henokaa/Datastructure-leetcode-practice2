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
            if i == len(nums):
                ans.append(path.copy())
                return
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)
            
            
            
        ans = []
        backtrack(0, [])
        return ans
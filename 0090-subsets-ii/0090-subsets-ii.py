class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(i, path):
            if i >= len(nums):
                ans.append(path.copy())
                return 
            
            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtracking(i + 1, path)
        
        
        ans = []
        nums.sort()
        print(nums)
        backtracking(0, [])
        return ans
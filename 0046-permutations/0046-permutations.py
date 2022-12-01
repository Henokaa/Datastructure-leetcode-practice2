class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, visited, path):
            path.append(nums[i])
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            visited.add(nums[i])
            for x in range(len(nums)):
                if nums[x] in visited:
                    continue
                backtrack(x, visited.copy(), path)
                path.pop()
            
                
        ans = []
        for i in range(len(nums)):
            backtrack(i, set(), [])
        
        return ans
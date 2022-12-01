class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i,visited, path):
            path.append(nums[i])
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            visited.add((nums[i],i))
            check = set()
            for x in range(len(nums)):
                if (nums[x],x) in visited or nums[x] in check:
                    continue
                check.add(nums[x])
                backtrack(x, visited.copy(), path)
                path.pop()
        
        
        ans = []
        checker2 = set()
        for i in range(len(nums)):
            if nums[i] in checker2:
                continue
            backtrack(i, set(), [])
            checker2.add(nums[i])
        return ans
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutation mean that in a one tree path we shouldn't repeat a number with 
        # the same position and number, one unique number each time
        def dfs(x, visited, path):
            path.append(x)
            # print(path, visited)
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            checker = set()
            for j in range(len(nums)):
                if (nums[j], j) in visited or nums[j] in checker:
                    continue
                visited.add((nums[j], j))
                checker.add(nums[j])
                dfs(nums[j], visited.copy(), path)
                visited.remove((nums[j],j))
                path.pop()
                
            
        
        ans = []
        
        checker2 = set()
        visited = set()
        path = []
        ans = []
        for i in range(len(nums)):
            if nums[i] in checker2:
                continue
            visited.add((nums[i], i))
            checker2.add(nums[i])
            dfs(nums[i], visited.copy(), [])
            visited.remove((nums[i],i))
        return ans
            
        
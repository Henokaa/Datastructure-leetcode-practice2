class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3]
        [1,2,3], [2,1,3], [3,2,1], [1,3,2], []
        '''
        prem = []
        ans = []
        visited = set()
        def dp(i, visited, prem):
            if i >= len(nums):
                return prem
            
            prem.append(nums[i])
            visited.add(nums[i])
            
            for x in range(len(nums)):
                if nums[x] not in visited:
                    dp(x, visited.copy(), prem.copy())
            if len(visited) == len(nums):
                ans.append(prem)
            return
            
        for i in range(len(nums)):
            dp(i, set(), [])
        return ans
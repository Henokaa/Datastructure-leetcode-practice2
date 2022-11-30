class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, path):
            
            path.append(candidates[i])
            
            total = sum(path)
            if total == target:
                ans.append(path.copy())
                return
                
            if total > target:
                return
            
            for x in range(i, len(candidates)):
                if total + candidates[x] <= target:
                    backtrack(x, path.copy())
                    # path.pop()
                    
        
        ans = []
        visited = set()
        for i in range(len(candidates)):
            backtrack(i, [])
        
        return ans
        
        
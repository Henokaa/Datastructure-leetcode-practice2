class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def backtrack(i, path):
            
            path.append(candidates[i])
            total = sum(path)
            if total == target:
                ans.append(path.copy())
                return
            visited2 = set()
            for x in range(i+1, len(candidates)):
                if total + candidates[x] <= target:
                    if candidates[x] not in visited2:
                        backtrack(x, path)
                        visited2.add(candidates[x])
                        path.pop()
                
                
        ans = []
        candidates.sort()
        visited1 = set()
        # print(candidates)
        for i in range(len(candidates)):
            if candidates[i] not in visited1:
                backtrack(i, [])
                visited1.add(candidates[i])
        
        return ans
        
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, path):
            if len(path) == k:
                ans.append(path.copy())
                return
            if i > n:
                return
            
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)
        
        ans = []
        backtrack(1, [])
        return ans
        
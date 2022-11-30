class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, path):
            path.append(i)
            if len(path) == k:
                ans.append(path.copy())
                return 
            
            if i > n:
                return
            
            
            for x in range(i + 1, n + 1):
                backtrack(x, path)
                path.pop()  
                
        ans = []
        for i in range(1, n+1):
            backtrack(i, [])
        return ans
        
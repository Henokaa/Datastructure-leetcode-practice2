class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(path, openN, closeN):
            
            if openN == n and closeN == n:
                ans.append("".join(path))
                return
            
            if openN < n:
                path.append("(")
                dfs(path, openN + 1, closeN)
                path.pop()
            
            if openN > closeN:
                path.append(")")
                dfs(path.copy(), openN, closeN + 1)
                path.pop()
        
        ans = []
        dfs([], 0, 0)
        return ans
                
                
            
                
                
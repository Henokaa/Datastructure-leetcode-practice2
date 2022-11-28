class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openN, closeN, path):
            if openN == n and closeN == n:
                res.append("".join(path.copy()))
            
            if openN + 1 <= n:
                path.append("(")
                dfs(openN + 1, closeN, path)
            
            if openN > closeN:
                path.append(")")
                dfs(openN, closeN + 1, path)
            
            path.pop()
            return
        res = []
        dfs(1,0,["("])
        return res
        
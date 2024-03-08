class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def dfs(opens, close, stack):
            if opens == n and close == n:
                bracket = "".join(stack)
                answer.append(bracket)
                return
            
            if opens < n:
                stack.append("(")
                dfs(opens + 1, close, stack)
                stack.pop()
                
            if close < opens and close < n:
                stack.append(')')
                dfs(opens, close + 1, stack)
                stack.pop()
        
        dfs(0,0, [])
        return answer
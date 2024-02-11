class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        '''
        answer = []
        def dfs(opens, closes, generated):
            if opens == n and closes == n:
                # print("answer")
                text = "".join(generated)
                answer.append(text)
                return  
            
            # print(opens, closes)
            if opens + 1 <= n:
                generated.append("(") 
                dfs(opens + 1, closes, generated)
                generated.pop()
            
            if closes + 1 <= n:
                if closes < opens:
                    generated.append(")")
                    dfs(opens, closes + 1, generated)
                    generated.pop()
                
            
        dfs(0,0, [])
        return answer
        
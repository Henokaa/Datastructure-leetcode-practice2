class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        1 - 1
        2 - 11
        3 - 21
        4 - 1211
        5 - 112121
        
        111221
              
                       
        '''
        def dfs(x):
            
            r = 0
            l = 0
            prev = x[0]
            answer = ""
            while r < len(x):
                if prev != x[r]:
                    length = r - l
                    answer += str(length) + str(prev)
                    l = r
                prev = x[r] 
                r += 1
            
            length = r - l
            answer += str(length) + x[-1]
            return answer
            
            
        # dfs(str(21))
        start = str(1)
        for i in range(n-1):
            output = dfs(str(start))
            start = output
        return start
            
            
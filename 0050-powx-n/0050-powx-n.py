class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        2 ^ 10
        
        2 ^ 5 ) ( 2 ^ 5)
        2  ^ 10
        
        time = logn
        
        '''
        def dfs(n):
            if n == 0:
                return 1
            
            if n % 2 == 0:
                temp = dfs(n // 2)
                return temp * temp
            
            else:
                return x * dfs(n-1)
            
        answer = dfs(abs(n))
        if n < 0:
            return 1 / answer
        else:
            return answer
        
        
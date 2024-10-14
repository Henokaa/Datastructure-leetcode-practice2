class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        x ^ n
        -2
        0(n)
        
        2.0 ^ 10
        
        return 2 * dfs(n - 1)
        
        10
        return x^5 * x^5
        
        x*x^4
        
        return x^2 * x^2
        
        '''
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x * x, n // 2)
            if n % 2 == 0:
                return res
            else:
                return x * res
            

        
        res = helper(x, abs(n))
        
        return res if n >= 0 else 1 / res
        
        
        
        
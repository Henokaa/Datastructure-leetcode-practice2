class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        [2,1,1]
        
        '''
        array = [0] * n
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        array[-1] = 1
        array[-2] = 1
        p1 = n - 3
        
        while 0 <= p1:
            array[p1] = array[p1+1] + array[p1 + 2]
            p1 -= 1
        
        
        return array[0] + array[1]
            
        
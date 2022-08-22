class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # i = n
        if n == 1:
            return True
        while n!= 0 and n % 4 == 0:
            n = n // 4
        
        if n == 1:
            return True
        else:
            return False
    
        # return (n & (n-1)) == 0 and (n & 0x55555555)
            
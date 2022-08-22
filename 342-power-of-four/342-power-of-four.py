class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # i = n
        # if n == 1:
        #     return True
        # while n:
        #     n = n / 4
        #     if n == 1.0:
        #         return True
        # return False
    
        return (n & (n-1)) == 0 and (n & 0x55555555)
            
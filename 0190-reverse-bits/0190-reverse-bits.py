class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ""
        res = 0
        for i in range(32):
            ans = n & 1
            res |= ans << (31 - i)
            n = n >> 1
    
        return res
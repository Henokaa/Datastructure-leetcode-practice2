class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        print(1 << 2)
        for i in range(32):
            bit = (n >> i) & (1)
            # bit = (n) & (1 << i) this will give you numbers like 4 when its in sec pos
            res |= (bit << (31 - i))
        return res
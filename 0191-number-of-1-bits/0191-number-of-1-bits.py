class Solution:
    def hammingWeight(self, n: int) -> int:
    
        res = 0
        count = 0
        while n:
            bit = n & 1
            if bit == 1:
                count += 1
            n = n >> 1
        return count
        
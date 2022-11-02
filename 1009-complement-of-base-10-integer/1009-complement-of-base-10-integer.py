class Solution:
    def bitwiseComplement(self, num: int) -> int:
        ans = 0
        base = 0
        i = 0
        while base <= num and i < 32:
            print((num >> i & 1))
            flipped = 1 - (num >> i & 1)
            ans = ans | flipped << i
            base = (1 << (i + 1))
            i += 1

       
        return ans
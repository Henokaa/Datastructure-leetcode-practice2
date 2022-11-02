class Solution:
    def bitwiseComplement(self, num: int) -> int:
        ans = 0
        n = 0
        for i in range(31, -1, -1):
            if num & 1 << i:
                n = i
                break
        for i in range(n + 1):
            res = 1 - (num >> i & 1)
            ans = ans | res << i

        return ans
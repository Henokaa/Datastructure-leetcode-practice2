class Solution:
    def climbStairs(self, n: int) -> int:
        n = n-1
        a = 1
        b = 1
        c = 1
        while n > 0:
            c = a + b
            b = a
            a = c
            n -= 1
        return c
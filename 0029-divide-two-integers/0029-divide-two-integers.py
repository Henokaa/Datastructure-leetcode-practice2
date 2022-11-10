class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if divisor == 1:
            return dividend
        negative = (dividend < 0) ^ (divisor < 0)
        dvd = abs(dividend)
        dvs = abs(divisor)
        res = 0

        while dvd >= dvs:
            tmp = dvs
            m = 1
            while (tmp << 1) <= dvd:
                tmp <<= 1
                m <<= 1  
            dvd -= tmp
            res += m

        if not negative:
            return res
        else:
            return ~res + 1
        
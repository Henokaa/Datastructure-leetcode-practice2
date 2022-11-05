class Solution:
    def isUgly(self, n: int) -> bool:
        primes = [2,3,5]
        if n == 0:
            return False
        for i in primes:
            while n % i == 0:
                n = n / i
        return True if n == 1 else False
        
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n + 1
        while r > l + 1:
            mid = l + (r - l)// 2
            cur = mid/2 * (mid + 1)
            if cur == n:
                return mid
            elif cur > n:
                r = mid
            elif cur < n:
                l = mid
                
        return l
        
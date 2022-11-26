class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num + 1
        while r > l + 1:
            mid = l + (r - l)//2
            cur = mid * mid
            if cur == num:
                return True
            elif cur > num:
                r = mid
            elif cur < num:
                l = mid
        return False
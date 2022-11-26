class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        [1,2,3,4]
        '''
        l = 0
        r = x
        # best = 0
        while l <= r:
            mid = l + (r - l)//2
            cur = mid * mid
            # print(mid, l, r)
            if cur == x:
                # print(mid)
                return mid
            elif cur > x:
                r = mid - 1
            elif cur < x:
                best = mid
                l = mid + 1
        return best
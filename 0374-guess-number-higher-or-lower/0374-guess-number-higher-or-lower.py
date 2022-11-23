# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = -1
        r = n + 1
        while r > l + 1:
            mid = l + (r - l)//2
            # print(mid, guess(mid))
            if guess(mid) == -1:
                r = mid
            elif guess(mid) == 1:
                l = mid
            else:
                return mid
            
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for n in nums:
            if n == 0:
                return 0
            if n<0:
                result = -result
        return result
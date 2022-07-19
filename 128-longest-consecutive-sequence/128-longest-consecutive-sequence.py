class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rep = set(nums)
        total = 0
        for i in nums:
            if i-1 not in rep:
                length = 0
                x = i
                while x in rep:
                    x = x+1
                    length += 1
                total = max(length, total)
        return total
        
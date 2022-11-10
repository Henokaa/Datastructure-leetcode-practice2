class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [x for x in freq if freq[x] == 1]
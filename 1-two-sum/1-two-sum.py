class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target - n in nums and i != nums.index(target - n):
                return i, nums.index(target - n)
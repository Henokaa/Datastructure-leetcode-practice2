class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i,x in enumerate(nums):
            ans ^= i ^ x
            
        return ans
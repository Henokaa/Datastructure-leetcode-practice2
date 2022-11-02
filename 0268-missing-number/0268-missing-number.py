class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        n = len(nums)
        totalsum = n *(n + 1)//2
        
        total = sum(nums)
        print(totalsum, total)
        
        return totalsum - total
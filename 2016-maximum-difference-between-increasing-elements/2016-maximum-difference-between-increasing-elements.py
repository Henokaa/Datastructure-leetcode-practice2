class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max=-1
        min=float('inf')
        for x in range(len(nums)):
            if nums[x]<min:
                min=nums[x]
            if nums[x]-min>max and nums[x]-min>0:
                max=nums[x]-min
        return max

        
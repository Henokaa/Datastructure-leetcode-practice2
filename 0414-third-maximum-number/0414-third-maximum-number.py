class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        nums=sorted(list(set(nums)))
        if len(nums)==2:
            return nums[1]
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==0:
            return None
        return nums[-3]
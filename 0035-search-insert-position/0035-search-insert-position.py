class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r > l + 1:
            mid = l + (r - l)// 2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid
            elif target < nums[mid]:
                r = mid
        return r
        
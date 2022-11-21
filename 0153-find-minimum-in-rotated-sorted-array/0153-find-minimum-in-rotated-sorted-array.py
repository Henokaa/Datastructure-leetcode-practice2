class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[l]:
            return nums[l]
        else:
            while l <= r:
                mid = l + (r - l)//2
                # print(mid)
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                elif nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        
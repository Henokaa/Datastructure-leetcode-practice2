class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums) - 1
        if nums[0] <= nums[length]:
            return nums[0]
        l = -1
        r = len(nums)
        right = float('inf')
        
        while r > l + 1:
            mid = l + (r - l)// 2
            # print(mid, l, r)
            if nums[mid] >= nums[0]:
                l = mid
            elif nums[mid] < nums[0]:
                r = mid
        
        return nums[r]
        
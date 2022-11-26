class Solution:
    def findMin(self, nums: List[int]) -> int:
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
        if r <= len(nums) - 1:
            right = nums[r]
        return min(right, nums[0])
        
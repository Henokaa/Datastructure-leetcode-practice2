class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = -1
        r = len(nums)
        length = len(nums)
        
        # if nums[0] > target > nums[r-1]:
        #     return -1
        while r > l + 1:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            print(mid)
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            elif nums[mid] < nums[0]:
                if nums[mid] < target <= nums[length-1]: # the equal important
                    l = mid
                else:
                    r = mid
                
        return -1
                
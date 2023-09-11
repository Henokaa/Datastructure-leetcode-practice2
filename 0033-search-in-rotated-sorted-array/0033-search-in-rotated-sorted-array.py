class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''I also did with while r > l + 1'''
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] < nums[0]:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
                    
        return -1
        
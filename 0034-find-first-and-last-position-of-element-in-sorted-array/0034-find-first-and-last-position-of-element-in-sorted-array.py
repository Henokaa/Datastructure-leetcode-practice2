class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        [5, 7, 7, 8, 8, 10]
               |                
        the starting point
        if mid > target:
            mif = r - 1
        '''
        l = 0
        r = len(nums) - 1
        start = float('inf')
        end = float('-inf')
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                start = min(start, mid)
                r = mid - 1
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                end = max(end, mid)
                l = mid + 1
                
        if start == float('inf'):
            return [-1, -1]
        else:
            return [start, end]
            
            
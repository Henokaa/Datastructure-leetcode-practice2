class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        [5, 7, 7, 8, 8, 10]
               |                
        the starting point
        if mid > target:
            mif = r - 1
        '''
        def binarymin(nums, target):
            left = 0
            right = len(nums) - 1
            start = float('inf')
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    start = mid
                    right = mid - 1
            if start == float('inf'):
                return -1
            else:
                return start
        def binarymax(nums, target):
            left = 0
            right = len(nums) - 1
            end = float('INF')
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    end = mid
                    left = mid + 1
            if end == float('inf'):
                return -1
            else:
                return end
        
        begin = binarymin(nums, target)
        end = binarymax(nums, target)
        return [begin, end]
            
        
        
        
            
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        [1,3]
         3
         
        '''
        l = 0
        r = len(nums) - 1
        length = len(nums)
        
        while l <= r:
            mid = l + (r - l)// 2
            # print(mid, l, r)
            if nums[mid] == target:
                return True
            # print(mid, l, r)
            while l < mid and nums[l] == nums[mid]:
                l += 1
                # if nums[l] == target:
                #     return True
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[length - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
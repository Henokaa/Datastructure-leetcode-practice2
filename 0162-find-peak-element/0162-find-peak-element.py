class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        [1,2,1,3,5,6,4]
                ^
         '''
        l = -1
        r = len(nums)
        if len(nums) == 1:
            return 0
        while r > l + 1:
            mid = l + (r - l) // 2
            print(mid, l ,r )
            if  mid-1 >= 0 and mid + 1 < len(nums) and nums[mid-1]< nums[mid] > nums[mid + 1]:
                return mid
            if mid + 1 >= len(nums) or mid-1  < 0:
                if mid + 1 >= len(nums) and nums[mid-1] < nums[mid]:
                    return mid
                elif mid-1 < 0 and nums[mid + 1] < nums[mid]:
                    return mid
                
            if (mid-1 < 0 or mid + 1 < len(nums)) and nums[mid] > nums[mid + 1]:
                print("a")
                r = mid
            else:
                l = mid
        
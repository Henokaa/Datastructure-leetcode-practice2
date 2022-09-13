class Solution:
    def minDifference(self, nums: List[int]) -> int:
        ''' We only need to find the max 4 and min 4 elements in nums, and It could be done by O(n) time without sorting (O(nlogn)).'''
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        L = len(nums) - 1
        '''[0,1, 5, 10, 14]
            '''
        return min(nums[L - 3] - nums[0],nums[L-2] - nums[1], nums[L- 1] - nums[2], nums[L] - nums[3] )
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        '''
        [1,2,2]
        
        [3,2,1,2,1,7]
        
        3:1
        2:2
        1:2
        7:1
        
        [1,1,1,0,0,0,1]
        1 -> 4
        2 -> 5
        
        
        [3,4,1,2,5,7]
        '''
        nums.sort()
        move = 0
        print(nums)
        
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                move += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
            # print(nums)
        return move
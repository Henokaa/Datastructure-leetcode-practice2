class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
        [3,2,4]
        target = 6
        
        [2, 3, 4]   => 6
         ^
            ^
        '''
        index = {}
        for i in range(len(nums)):
            index[i] = nums[i]
        
        sorted_num = sorted(index.items(), key = lambda x:x[1])
        
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            number = sorted_num[l][1] + sorted_num[r][1]
            if number == target:
                return [sorted_num[l][0], sorted_num[r][0]]
            elif number > target:
                r -= 1
            else:
                l += 1
        
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
        [3,2,4]
        target = 6
        
        [2, 3, 4]   => 6
         ^
            ^
            
        [3,2,4]
        
        
        
        [3, 3]
        
        3:1
        
        
        '''
        hashmap = {}
        
        for i in range(len(nums)):
            number = target - nums[i]
            if number in hashmap:
                return [i, hashmap[number]]
            
            hashmap[nums[i]] = i
        
        return []
        
        
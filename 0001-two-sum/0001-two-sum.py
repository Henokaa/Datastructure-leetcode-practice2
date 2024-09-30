class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
        [3,2,4]
        target = 6
        
        [2, 3, 4]   => 6
         ^
            ^
        '''
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        print(hashmap)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
        
        
        
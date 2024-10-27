class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        understand
        
        
        constraint
        
        naive approach
        [2,7,11,15]  = 9
           ^
        iterate
            visted,add
            check
        
        optimal 
        
        edge
    
        '''
        visited = {}
        for i in range(len(nums)):
            
            number = target - nums[i]
            if number in visited:
                return [visited[number], i]
            visited[nums[i]] = i
        
            
        
        
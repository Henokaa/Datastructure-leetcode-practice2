class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set(nums)
        i = 1
        while True:
            if i not in visited:
                return i
            
            i += 1
            
    
            
        
                
                
            
        
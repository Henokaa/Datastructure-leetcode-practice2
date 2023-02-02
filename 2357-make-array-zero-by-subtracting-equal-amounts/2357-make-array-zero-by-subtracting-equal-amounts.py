class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        current = 0
        
        for x in nums:
            x -= current
            
            if x > 0:
                current += x
                count += 1
                
        return count
        
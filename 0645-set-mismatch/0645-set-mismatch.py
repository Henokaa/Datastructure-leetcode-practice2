class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        saved = Counter(nums)
        # print(saved)
    
        for i in range(1, len(nums)+1):
            
            if i not in saved: 
                missed = i
            
            elif saved[i] > 1:
                repeated = i
        
        return [repeated, missed]
            
            
        
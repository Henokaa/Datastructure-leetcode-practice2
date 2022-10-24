class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        To understand this question, you have to understand how remainders work. If k = 5, then 6 % 5 = 1, which also means (6 + 5) % 5 = 1. So you use a hash map to check if you have seen that remainder before. If yes, then you know between both indexes, it is 5 (i.e. (6 + 5) - 6 = 5). This question tests nothing other than knowing how remainders work.
        eg - 23 % 6 = 5
        (23 + 2 + 4)% 5 = 5 so 2 + 4 is multiple of 5
        '''
        
        remainder = { 0: -1 }
        total = 0
        
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
                
            elif i - remainder[r] > 1:
                return True
        return False
        
        
        
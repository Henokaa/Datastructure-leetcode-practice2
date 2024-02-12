class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        [2,2,1,1,1,2,2]
        Boyer-Moore Voting Algorithm
        '''
        count = {}
        res, maxCount = 0, 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(maxCount, count[n])
        
        
        return res

        
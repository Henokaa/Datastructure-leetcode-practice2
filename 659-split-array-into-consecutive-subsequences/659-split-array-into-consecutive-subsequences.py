class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        r = 0
        array1 = []
        array2 = []
        '''
        [1, 2, 2, 3, 4, 5]
        [1, 2, 3
        [2, 
        [3, 4, 5
        '''
        
        ones = Counter()
        twos = Counter()
        threes = Counter()
        
        
        for x in nums:
            if ones[x - 1] > 0:
                ones[x - 1] -= 1
                twos[x] += 1
                continue
            
            if twos[x - 1] > 0:
                twos[x - 1] -= 1
                threes[x] += 1
                continue
            
            if threes[x - 1] > 0:
                threes[x - 1] -= 1
                threes[x] += 1
                continue
            
            ones[x] += 1
        
        if ones.total() > 0 or twos.total() > 0:
            return False
        return True
            
                
        
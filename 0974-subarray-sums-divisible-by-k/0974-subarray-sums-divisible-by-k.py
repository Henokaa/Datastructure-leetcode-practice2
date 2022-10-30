class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        [4, 5, 0, -2, -3, 1]
         
        
        [4, 9, 9, 7, 4, 5]
        [4, 4, 4, 2, 4, 0]
        
        [4, 5, 5]
        [4, 9, 14]
        [4, 4, 2]
        
        '''
        
        r = 0
        total = 0
        saved = defaultdict(int)
        ans = 0
        
     
        while r < len(A):
            total += A[r]
            curr = total % K
            if curr in saved:
                ans += saved[curr]
            if curr == 0:
                ans += 1
            saved[curr] += 1
            r += 1
            
        return ans
            
        
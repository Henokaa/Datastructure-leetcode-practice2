class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        sort
        start and end
        if possible -> mid
            l = mid
        
        
        
        ---
        6
        
        '''
        position.sort()
        # print(position)
        l = 1
        r = position[-1] - position[0]
        
        def valid(mid):
            count = 0
            prev = float('-inf')
            for i in range(len(position)):
                if position[i] >= prev + mid:
                    prev = position[i]
                    count += 1
                    
            if count >= m:
                return True
            return False
                
        while l <= r:
            mid = l + (r - l) // 2
            # print(mid)
            if valid(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
                
        return ans
            
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        _, 
        '''
        # Sort the positions
        position.sort()
        
        def isPossible(x):
            count = 1
            prev = position[0]
            for p in position:
                if p - prev >= x:
                    prev = p
                    count += 1
            if count >= m:
                return True
            return False
        
        l = 1
        r = position[-1] - position[0]
        # print(position, l, r)
        while l <= r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                l = mid + 1
                answer = mid
            else:
                r = mid - 1
        
        return answer
        
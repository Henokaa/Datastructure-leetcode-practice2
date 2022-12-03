class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        [1,2,3]
        
        [6,3,2]
        
        
        [1 - 5]
        '''
        
        l = 0
        r = totalTrips*time[0] + 1
        while r > l + 1:
            mid = l + (r - l)//2
            total = 0
            
            for i in time:
                total += mid // i 
            
            # print(mid, total)
            if total >= totalTrips:
                r = mid
            if total < totalTrips:
                l = mid
        return r
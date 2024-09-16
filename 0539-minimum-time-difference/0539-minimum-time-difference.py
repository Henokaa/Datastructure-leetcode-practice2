class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        '''
        sec 
        sort
        check , first and last
        
        '''
        time_dif = []
        for i in range(len(timePoints)):
            time = timePoints[i]
            hr, minute = time.split(":")
            cur_time = int(hr)*60 + int(minute)
            time_dif.append(cur_time)
            
        time_dif.sort()
        
        l = 0
        r = 1
        min_time = float('inf')
        while r < len(time_dif):
            temp_time = time_dif[r] - time_dif[l]
            
            min_time = min(min_time, temp_time)
            
            r += 1
            l += 1
        
        if len(time_dif) > 1:
            min_time = min(min_time, time_dif[-1] - time_dif[0], 1440 - time_dif[-1] + time_dif[0])
            
        return min_time
            
        
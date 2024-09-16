class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minute_list = []
        for time in timePoints:
            hour, minute = time.split(':')
            minute_list.append(int(hour)*60 + int(minute))
        
        
        minute_list.sort()
        min_diff = float('inf')
        
        r = 1
        l = 0
        while r < len(minute_list):
            min_diff = min(min_diff, minute_list[r] - minute_list[l])
            r += 1
            l += 1
        
        min_diff = min(min_diff, 1440 - minute_list[-1] + minute_list[0])
       
        
        return min_diff
            
        
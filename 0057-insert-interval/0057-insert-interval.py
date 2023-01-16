class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        cur = 0
        res = []
        res.append([-1,-1])
        if len(intervals) == 0:
            return [newInterval]
        while cur < len(intervals):
            if intervals[cur][0] < newInterval[0]: 
                res.append(intervals[cur])
            else:
                l = newInterval[0]
                r = newInterval[1]
                if res[-1][0] <= newInterval[0] <= res[-1][1]:
                    l = res[-1][0]
                    r = max(newInterval[1], res[-1][1])
                    res.pop()
              
                while cur < len(intervals) and l <= intervals[cur][0] <= r:
                    r = max(intervals[cur][1], r)
                    cur += 1
                
                res.append([l,r])
                while cur < len(intervals):
                    res.append(intervals[cur])
                    cur += 1
                return res[1:]
            cur += 1 
    
        l = newInterval[0]
        r = newInterval[1]
        if res[-1][0] <= newInterval[0] <= res[-1][1]:
            l = res[-1][0]
            r = max(newInterval[1], res[-1][1])
            res.pop()
        res.append([l,r])
        return res[1:]
        
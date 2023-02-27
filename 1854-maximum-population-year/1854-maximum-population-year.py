class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = []
        end = []
        for i in range(len(logs)):
            start.append(logs[i][0])
            end.append(logs[i][1])
        
        p1 = 0
        p2 = 0
        count = 0
        mxcount = -1
        start.sort()
        end.sort()
        # print(start)
        # print(end)
        while p1 < len(start) and p2 < len(end):
            if start[p1] < end[p2]:
                count += 1
                p1 += 1
            elif end[p2] <= start[p1]:
                count -= 1
                p2 += 1
            if count > mxcount:
                print(count, p1, p2)
                mxcount = max(mxcount, count)
                ans = start[p1-1]
                
        return ans
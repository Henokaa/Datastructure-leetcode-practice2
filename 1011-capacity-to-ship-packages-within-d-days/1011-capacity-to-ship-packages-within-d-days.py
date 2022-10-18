class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        mx = max(weights)
        capacity = [i for i in range(mx, total + 1)]
        l = 0
        r = len(capacity)
        '''
        2 - 5
        '''
        answer = 0
        while l <= r:
            mid = l + (r - l)//2
            capsum = 0
            curday = 1
            for i in weights:
                capsum += i
                if capsum > capacity[mid]:
                    curday += 1
                    capsum = i
                    
    
            if curday <= days <= len(capacity):
                answer = capacity[mid]
                
            if curday  > days:
                l = mid + 1
            elif curday == days:
                r = mid - 1
            elif curday < days:
                r = mid - 1
                
        return answer
            
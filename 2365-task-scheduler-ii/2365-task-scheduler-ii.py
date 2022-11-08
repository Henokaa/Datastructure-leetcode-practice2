class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        '''
        1,2,_,_,1,2,3,_, 1
                    ^
        c = 1
        visited = (1,0),(2,1) (elem,r)
        r + c
        [1,2,1,2,3,1]
             ^
        '''
        # start iterating
        current = 0
        saved = {}
        r = 0
        while r < len(tasks):
            if tasks[r] in saved:
                current = max(saved[tasks[r]] + space + 1,current)
                # print(current, tasks[r])
                saved[tasks[r]] = current
                current += 1
                r += 1
            else:
                saved[tasks[r]] = current
                current += 1
                r += 1
 
        return current 
        
        
        
        
        
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        '''
        [1,2,_,_,1,2,3,_,1]
                 ^
        1: 3
        2: 1
        3: 6
        
        val = 1 + 4 = 5
        = 3 + 4 = 7
        
        
        temp = max(temp, val)
        temp += 1
        
        [1,2,1,2,3,1]
                 ^
        '''
        saved = {} 
        r = 0
        temp = 0
        while r < len(tasks):
            if tasks[r] not in saved:
                saved[tasks[r]] = temp
            else:
                val = saved[tasks[r]] + space + 1
                temp = max(temp, val)
                saved[tasks[r]] = temp
            r += 1
            temp += 1
        
        return temp
            
        
        
        
        
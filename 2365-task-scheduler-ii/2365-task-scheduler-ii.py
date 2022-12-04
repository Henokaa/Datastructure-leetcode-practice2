class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        '''
        [1,]
        '''
        saved = {}
        time = 0
        for i in range(len(tasks)):
            
            if tasks[i] in saved:
                temp = saved[tasks[i]]
                time = max(time + 1, temp)
                saved[tasks[i]] = time + space + 1
            
            else:
                time += 1
                saved[tasks[i]] = time + space + 1
                
            # print(i , time)
            
        return time
                
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap
        '''
        for range of n:
            pop
            saved in array
            or idle
        add it in saved in heap
        '''
        max_heap = []
        count = 0
        if n == 0:
            return len(tasks)
        tasks = Counter(tasks)
        
        
        for x,y in tasks.items():
            heapq.heappush(max_heap, [-y,x])
        
        while max_heap:
            i = n + 1
            temp = []
            
            while i > 0:
                if max_heap:
                    num, char = heapq.heappop(max_heap)
                    if num + 1 < 0:
                        temp.append([num + 1, char])
                    count += 1
                    
                elif len(temp) > 0:
                    count += 1
    
                i -= 1
            
            
            for x,y in temp:
                if x < 0: 
                    heapq.heappush(max_heap, [x,y])
            # print(max_heap)
                
        return count
            
                
            
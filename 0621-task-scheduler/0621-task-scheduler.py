class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        A - 3
        b - 0
        c - 0
        d - 0
        e - 0
        f - 0
        g - 0
        AbCAdeAfgA _ _ A _ _ A
        '''
        #Counter
        tasks = Counter(tasks)
        maxHeap = []
        for x, y in tasks.items():
            heapq.heappush(maxHeap, [-y, x])
        
        # while maxHeap
        i = 0
        n = n + 1
        que = []
        ans = 0
        while maxHeap:
            while i < n:
                if not maxHeap and not que:
                    break
                if maxHeap:
                    value, char = heapq.heappop(maxHeap)
                    i += 1
                    ans += 1
                    value += 1
                    if value != 0:
                        que.append([value, char])
                else:
                    ans += 1
                    i += 1
            
            for x, y in que:
                heapq.heappush(maxHeap, [x, y])
            que = []
            i = 0 
        return ans
                
                
            
        
        # if empty go until n times and increment
        # array append the poped
        # if it is 0 don't add
        
    
        
    
        
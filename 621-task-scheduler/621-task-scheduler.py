class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        
        '''
        heap1 = []
        que = []
        count = Counter(tasks)
    
        for x,y in count.items():
            heap1.append([-y, x])
        heapq.heapify(heap1)
        
        ans = 0
        while heap1:
            i = 0
            while i < n + 1:
                if heap1 or que: 
                    ans += 1
                if heap1:
                    times, element = heapq.heappop(heap1)
                    times = times + 1
                    if times != 0:
                        que.append([times, element]) 
                i += 1
            for x, y in que:
                if x == 0:
                    continue
                heapq.heappush(heap1, [x, y])
            que = []
        return ans
    
        
    
        
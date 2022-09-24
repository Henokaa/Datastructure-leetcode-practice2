class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Time-complexity - o(n) also if m idle time and if all element is 'A' 0(n * m)
        i suggest o(nlogn) because we will pop every element
        '''
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        
        time = 0 
        q = deque()
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = -heapq.heappop(maxHeap) - 1
                if cnt:
                    q.append([-cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
    
        
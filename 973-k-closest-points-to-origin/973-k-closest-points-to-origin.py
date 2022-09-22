class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Typical heap solution:	heapify costs O(n), heappop on k elements costs O(k * logn)	O(n + k * logn)
This heap solution:	heappushpop on n elements costs O(n * logk)	O(n * logk) 
        '''
        heap = []
        
        for (x, y) in points:
            dist = (x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (-dist, x, y))
            else:
                heapq.heappush(heap, (-dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
        
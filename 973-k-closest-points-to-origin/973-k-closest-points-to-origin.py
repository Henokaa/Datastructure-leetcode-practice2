class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        [[1,3, 10], [-2, 2, 8]]
        (1, 8)       
        '''
        heap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            d = (x ** 2) + (y ** 2)
            heap.append([d, i])
        heapq.heapify(heap)
        ans  = []
        for i in range(k):
            d, x = heapq.heappop(heap)
            ans.append(points[x])
        return ans
        
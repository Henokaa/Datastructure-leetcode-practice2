class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        a = []
        for point in points:
            print(point)
            x,y = point[0],point[1]
            d = (x*x + y*y)
            heap.append([x,y,d])
        
        heap.sort(key = lambda x : x[2])
    
       # return heap
        for x in range(k):
            a.append(heap[x][0:2])
        return a
    
            
        
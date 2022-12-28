class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for x in piles:
            heapq.heappush(heap, -x)
            
        print(heap[0])
        while k > 0:
            elem = heapq.heappop(heap)
            elem = -elem
            elem = elem - (elem // 2)
            heapq.heappush(heap, -elem)
            k -= 1
        
        return -sum(heap)
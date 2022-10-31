class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        [4,12,2,7,3,18,20,3,19]
                          ^
        
        '''
        heap = []
        def push(x):
            heapq.heappush(heap, -x)
        def pop():
            return -heapq.heappop(heap)
        # go to the next one we first check brick then use ladder 
        r = 0
        diff = 0
        
        
        while r < len(heights):
            if r + 1 < len(heights):
                diff = heights[r+1] - heights[r]
            else:
                return r
            if diff > 0:
                bricks -= diff
                push(diff)
                
                if ladders > 0 and bricks < 0:
                    while ladders > 0 and len(heap) != 0 and bricks < 0:
                        bricks += pop()
                        ladders -= 1
                elif ladders <= 0 and bricks < 0:
                    return r
        
            r += 1
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for x,y,w in flights:
            graph[x].append((y,w))
        
        que = []
        que.append((0, src, 0))
    
        min_cost = {(src, 0) : 0}
        
        while que:
            total, src, level = heapq.heappop(que) 
            if src == dst:
                return total
            
            if level + 1 <= k + 1:
                for y,w in graph[src]:
                    if ((y, level + 1) in min_cost and min_cost[(y, level + 1)] > w + total) or (y, level + 1) not in min_cost:
                        min_cost[(y, level + 1)] = w + total
                        heapq.heappush(que, (w+total, y, level+1))
                
                    
        return -1
            
                
            
        
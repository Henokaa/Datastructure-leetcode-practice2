class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        k += 1
        
        graph[0] = (1, 100)
        dijkstra
        heapq.heappush(que, (cost, node, temp_level))
        visited [{node, level}] = cost
        '''
        graph = defaultdict(list)
        for x,y,z in flights:
            graph[x].append((y, z))
        
    
        que = []
        level = 0
        visited = {}
        que.append((0, src, 0))
        visited[(src, 0)] = 0
        while que:
            cost, node, temp_level = heapq.heappop(que)
            
            if temp_level - 1 > K:
                continue
                
            if node == dst and (temp_level - 1) <= K:
                return cost
            
            for child, child_cost in graph[node]:
                if ((child, temp_level + 1) in visited and visited[(child, temp_level + 1)] <= cost + child_cost):
                    continue
                    
                heapq.heappush(que, (cost + child_cost, child, temp_level + 1))
                visited[(child, temp_level + 1)] = cost + child_cost
            
        
        
        return -1
            
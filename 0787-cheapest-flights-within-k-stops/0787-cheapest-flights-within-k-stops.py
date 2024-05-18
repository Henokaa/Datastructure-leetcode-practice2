class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        graph
        
        dikstra
        
        visit
        '''
        graph = defaultdict(list)
        for x,y,weights in flights:
            graph[x].append((y, weights))
        
        # print(graph)
        visited = {}
        que = []
        que.append((0, src, 0))
        level = 0

        visited[(src, level)] = 0
        
        while que:
            weight, temp, temp_level = heapq.heappop(que)
            # print(weight, temp)
            if temp_level > k + 1:
                continue
                
            if temp == dst:
                return weight
            
            
            
            for child in graph[temp]:
                if  ((child[0], temp_level+1) in visited and visited[child[0], temp_level+1] <= child[1] + weight):
                    continue
                # print(child)
                # if ((child[0], temp_level+1) in visited and visited[child[0], temp_level+1] > child[1] + weight) or (child[0], temp_level+1) not in visited:
                heapq.heappush(que, (child[1] + weight, child[0], temp_level + 1))
                visited[(child[0], temp_level + 1)] = child[1] + weight
                
            level += 1
            
        return -1
            
            
            
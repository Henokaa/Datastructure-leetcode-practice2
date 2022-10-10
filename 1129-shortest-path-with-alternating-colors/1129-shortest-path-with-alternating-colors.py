class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        redgraph = defaultdict(list)
        bluegraph = defaultdict(list)
        for edges in redEdges:
            redgraph[edges[0]].append(edges[1])
            
        for edges in blueEdges:
            bluegraph[edges[0]].append(edges[1])
        
        array = [float('INF')] * n
        array[0] = 0
        que = deque()
        if 0 in redgraph:
            for x in redgraph[0]:
                que.append((x,"r"))
        if 0 in bluegraph:
            for x in bluegraph[0]:
                que.append((x,"b"))
        level = 1
        
        visited = set()
        while que:
            length = len(que)
            
            for i in range(length):
                x, c = que.popleft()
                if (x,c) not in visited:
                    visited.add((x,c))
                    array[x] = min(array[x], level)
                    if c == "r":
                        graph = bluegraph
                        color = "b"
                    else:
                        graph = redgraph
                        color = "r"
                    for z in graph[x]:
                        que.append((z, color))
            level += 1
        for x,y in enumerate(array):
            if y == float('INF'):
                array[x] = -1
                
        return array
                    
                        
                    
                    
            
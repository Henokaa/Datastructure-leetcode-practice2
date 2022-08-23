class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # adjacency list and the actual list
        graph = defaultdict(set)
        adjacent = defaultdict(set)
        
        for x,y in connections:
            graph[x].add(y)
            adjacent[x].add(y)
            adjacent[y].add(x)
            
        que = deque()
        que.append((0, -1))
        res = 0
        while que:
            var, prev = que.pop()
            for child in adjacent[var]:
                if child == prev:
                    continue
                if var not in graph[child]:
                    res += 1
                que.append((child, var))
                
        return res
                    
                    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        x = popleft()
        parent blue1
        
        children green2
        
        if parent is blue the children must be green
        it must never be the same color
        '''
        node = {}
        for i in range(len(graph)):
            node[i] = graph[i]
        
        que = deque()
        visited1 = {}
        for i in range(len(graph)):
            if i in visited1:
                continue
            visited1[0] = 0
            que = deque()
            que.append((i, 0))
            
            while que:
                parent = que.popleft()
                
                for x in graph[parent[0]]:
                    if x not in visited1:
                        if parent[1] == 1:
                            visited1[x] = 0
                            que.append((x, 0))
                        else:
                            visited1[x] = 1
                            que.append((x, 1))
                    else:
                        if visited1[x] == parent[1]:
                            return False
                        
        return True
            
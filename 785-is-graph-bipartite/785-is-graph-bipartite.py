class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = defaultdict(list)
        visited = {}
        for i in range(len(graph)):
            nodes[i].append(graph[i])
        
        def biparte(x):
            que = deque()
            que.append((x, 1))
            
            while que:
                temp = que.pop()
                visited[temp[0]] = temp[1]

                for i in graph[temp[0]]:
                    if i in visited:
                        if temp[1] == visited[i]:
                            return False
                    else:
                        color = 0 if temp[1] == 1 else 1
                        que.append((i, color))
            return True
            
        
        for x in range(len(graph)):
            if x not in visited:
                if not biparte(x):
                    return False
        return True
            
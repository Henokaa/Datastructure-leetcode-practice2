class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        coloring
        '''
        # graph
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = {}
        for start in graph.keys():
            que = deque()
            if start in visited:
                continue
            que.append((start, 0))
            visited[start] = 0
            while que:
                parent = que.popleft()
                for child in graph[parent[0]]:
                    if child not in visited:
                        if parent[1] == 0:
                            que.append((child, 1))
                            visited[child] = 1
                        else:
                            que.append((child, 0))
                            visited[child] = 0
                    else:
                        if visited[child] == visited[parent[0]]:
                            return False
        return True
                        
        # coloring with a set
                    
            
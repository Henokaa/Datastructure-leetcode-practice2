class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        graph
        que 
        parent and child must be different color
        
        '''

        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        '''it must be undirectional if you assume it is not connected and check every key
        because we start by assumung the first node is 0'''
        # print(graph)
        visited = {}
        que = deque()
        
        for x in graph.keys():
            
            if x in visited:
                continue
                
            visited[x] = 0
            que.append((x,0))
            while que:
                parent = que.popleft()
        
                if parent[0] in graph:
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
                        
                        
                    
            
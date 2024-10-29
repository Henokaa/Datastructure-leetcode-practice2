class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        constraint
            
        visted[node] = color
        for 
            if not visited
                que.append (node, 0)
                    while que
                        node
                            for child 
                                if child in visited:
                                    visited[child] == color
                                        return False
                                    
        
        edge case
        
        '''
        visited = {}
        que = deque()
        for elements in range(len(graph)):
            if elements not in visited:
                color = 0
                que.append((elements, color))
                while que:
                    node, new_color = que.popleft()
                    visited[node] = new_color
                    for child in graph[node]:
                        if child in visited:
                            if visited[child] == new_color:
                                return False
                        else:
                            if new_color == 1:
                                que.append((child, 0))
                    
                            else:
                                que.append((child, 1))
        
        return True
                            
        
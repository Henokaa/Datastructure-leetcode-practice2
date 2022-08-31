class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        white = 0
        red = 1
        blue = 2
        colors = [white] * n
        
        def goColor(start):
            q = collections.deque()
            colors[start] = red
            q.append((red, start))
            
            while len(q) > 0:
                currentColor, x = q.popleft()
                nextColor = (red if currentColor == blue else blue)
                
                for v in graph[x]:
                    if colors[v] == white:
                        colors[v] = nextColor
                        q.append((nextColor, v))
                    elif colors[v] != nextColor:
                        return False
                    
            return True
        
        
        for x in range(n):
            if colors[x] == white:
                if not goColor(x):
                    return False
        return True
        
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        grid = {}
        visited = set()
        seen = set()
        
        for i in range(len(graph)):
            grid[i] = []   # not grid[i].append([])
            
            
        for i in range(len(graph)):
            for j in graph[i]:
                grid[i].append(j)
        print(grid)
        def dfs(i):
            if i in visited:
                return False
            if i in seen:
                return True
            visited.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return 
            visited.remove(i)
            seen.add(i)
            return seen
        
        for i in range(len(graph)):
            dfs(i)
                
        return sorted(seen)
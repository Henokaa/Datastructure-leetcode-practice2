class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        ans = []
        def dfs(i, path):
            if i == len(graph) - 1:
                ans.append(path.copy())
                return
            
            
            for child in graph[i]:
                path.append(child)
                dfs(child, path)
                path.pop()
                
        
        dfs(0, [0])
                
        return ans
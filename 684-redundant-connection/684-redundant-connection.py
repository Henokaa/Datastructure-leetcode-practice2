class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(s,d): #Measures if s and d CAN be connected directly or indirectly.
            if s not in seen:
                seen.add(s)
                if s==d:
                    return True
                return any(dfs(n,d) for n in graph[s])
            return False
        
        for u,v in edges:
            seen =set() #Cause we dont want to have infinite loops.
            if dfs(u,v): #If u and v ARE already conected, then we dont want a redundant edge.
                return [u,v]
                
            graph[u].add(v)
            graph[v].add(u)
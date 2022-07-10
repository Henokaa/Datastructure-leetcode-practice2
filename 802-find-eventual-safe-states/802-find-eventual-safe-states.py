class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        matrix = {}
        indegree = {}
        s = deque()
        ans = []
        for i in range(len(graph)):
            matrix[i] = []
            indegree[i] = 0
            
            
        for i in range(len(graph)):
            for j in graph[i]:
                matrix[j].append(i)
                indegree[i] += 1
        
        
        
        for i, j in indegree.items():
            if j == 0:
                s.append(i)
    
        while s:
            a = s.popleft()
            ans.append(a)
            for i in matrix[a]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    s.append(i)
        return sorted(ans)
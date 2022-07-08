class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = {}
        q = deque()
        ans = []
        
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
            
        temp = prerequisites
        for x in temp:
            graph[x[0]].append(x[1])
            indegree[x[1]] += 1 
            
        for a,b in indegree.items():
            if b == 0:
                q.append(a)
            
        while q:
            s = q.popleft()
            ans.append(s)
            for v in graph[s]:
                indegree[v] -= 1 
                if indegree[v] == 0:
                    q.append(v)
                    
        if len(ans) == numCourses: # Attention
            return ans[::-1]
        else:
            return []
            
            
        
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {}
        que = deque()
        visited = set()
        for i in range(numCourses):
            indegree[i] = 0
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        for x,y in indegree.items():
            if y == 0:
                que.append(x)
                visited.add(x)
       
        answer = []
    
        while que:
            element = que.popleft()
            answer.append(element)
            
            for child in graph[element]:
                indegree[child] -= 1
                if child not in visited and indegree[child] == 0:
                    que.append(child)
                    visited.add(child)
                    
        return answer if len(answer) == numCourses else []
        
        
            
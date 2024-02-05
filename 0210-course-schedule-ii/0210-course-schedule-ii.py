class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        '''
        visited = set()
        graph = defaultdict(list)
        indegree = {}
        for i in range(numCourses):
            indegree[i] = 0
            
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
            
        que = deque()
        for x,y in indegree.items():
            if y == 0:
                que.append(x)
                visited.add(x)
                
        
        # print("indegree", indegree)
        print(que)
        ans = []
        while que:
            length = len(que)
            
            for i in range(length):
                item = que.popleft()
                ans.append(item)
                for course in graph[item]:
                    indegree[course] -= 1
                    if indegree[course] == 0 and course not in visited:
                        que.append(course)
                        visited.add(course)
         
        return ans if len(ans) == numCourses else []
                
            
        
        
            
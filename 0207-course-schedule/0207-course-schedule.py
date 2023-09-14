class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for x,y in prerequisites:
            indegree[x] += 1
            graph[y].append(x)
        
        que = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
        # print(que)    
        while que:
            temp = que.popleft()
            numCourses -= 1
            for i in graph[temp]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)
                    
        # print(numCourses, graph)   
        if numCourses == 0:
            return True
        else:
            return False
            
            
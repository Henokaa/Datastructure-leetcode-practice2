class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        red = set()
        green = set()
        for x, y in prerequisites:
            graph[x].append(y)
            
        
        def dfs(i):
            if i in red:
                return False
            if i in green:
                return True
            red.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            red.remove(i)
            green.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

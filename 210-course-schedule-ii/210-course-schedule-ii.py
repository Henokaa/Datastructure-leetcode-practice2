class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        c = 0
        cycle = set()
        visited = set()
        output = []
        for i in range(len(prerequisites)):
            preMap[prerequisites[i][c]].append(prerequisites[i][c+1])
        
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for x in preMap[i]:
                if not dfs(x):
                    return False
            #if all the children pass and no false
            
            cycle.remove(i)
            visited.add(i)
            output.append(i)
            return True
            
        for i in range(numCourses):
            
            if not dfs(i): # from the children is there any that return false
                return []
        return output
            
            
        
        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        que = deque()
        visited = set()
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
            
        for i in range(len(indegree)):
            if indegree[i] < 2:
                que.append(i)
                visited.add(i)
                

        
        while que:
            length = len(que)
            ans = []
            for i in range(length):
                temp = que.popleft()
                ans.append(temp)
                for x in graph[temp]:
                    if x not in visited:
                        indegree[x] -= 1
                        if indegree[x] < 2:
                            que.append(x)
                            visited.add(x)
            

        return ans
                
                        
                
            
            
        
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        graph[y].append(x)
        indegree[x] += 1
        
        '''
        edges = defaultdict(list)
        indegree = {}
        for i in range(len(graph)):
            indegree[i] = 0 
            for j in range(len(graph[i])):
                edges[graph[i][j]].append(i)
                indegree[i] += 1

        # print(edges)
        # print(indegree)
        que = deque()
        for x,y in indegree.items():
            if y == 0:
                que.append(x)
        
        # print(que)
        ans = []
        while que:
            output = que.popleft()
            ans.append(output)
            for child in edges[output]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)
             
        ans.sort()
        return ans
            
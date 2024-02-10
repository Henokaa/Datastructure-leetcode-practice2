class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i):
            seen[i] = True
            for j in graph[i]:
                if not seen[j]:
                    dfs(j)

        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                # print(i,x, y)
        
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        # print(graph)

        seen = [False] * len(stones)
        islands = 0
        for i in range(len(stones)):
            if not seen[i]:
                dfs(i)
                islands += 1

        return len(stones) - islands
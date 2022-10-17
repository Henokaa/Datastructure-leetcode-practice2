class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
         [
         [9,10,4],
         [7,6,5],
         [2,1,1]
         ]
         
        '''
        graph = defaultdict(list)
        row = len(matrix)
        cols = len(matrix[0])
        indegree = [[0] * cols for i in range(row)]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        inbound = lambda r,c: 0<=r<len(matrix) and 0<=c<len(matrix[0])
        que = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for x,y in directions:
                    nr = i + x
                    nc = j + y
                    if inbound(nr,nc) and matrix[i][j] < matrix[nr][nc]:
                        graph[(i,j)].append((nr,nc))
                        indegree[nr][nc] += 1
        
        for i in range(len(indegree)):
            for j in range(len(indegree[0])):
                if indegree[i][j] == 0:
                    que.append((i,j))
        
        # print(que)
        level = 0
        while que:
            length = len(que)
            for i in range(length):
                temp = que.popleft()
                for x in graph[temp]:
                    indegree[x[0]][x[1]] -= 1
                    if indegree[x[0]][x[1]] == 0:
                        que.append((x[0],x[1]))
                        
            level += 1
        
        return level
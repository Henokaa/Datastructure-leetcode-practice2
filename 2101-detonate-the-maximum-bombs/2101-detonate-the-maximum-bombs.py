class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''
        Time - o(n^2)
        space - o(n) recursion stack, visited set
        
        for bombs
            bfs()

        bfs()
            ->
            index
                sort by distance
                for detonate in bombs
                add it in que
                
                
        Time = 0(n^3)
        '''
        que = deque()
        
        def bfs(x,y,r,i):
            index = (x,y,r,i)
            que.append((x,y,r))
            count = 0
            visited = set()
            visited.add(i)
            while que:
                # print(que, count)
                current = que.popleft()
                
                count += 1
                
                for i, bomb in enumerate(bombs):
                    x,y,r = bomb
                    distance = sqrt((current[0] - x)**2 + (current[1] - y)**2)
                    if i not in visited and distance <= current[2]:
                        que.append((x,y,r))
                        visited.add(i)
                
            return count
            
        maximum_answer = 0
        for i,bomb in enumerate(bombs):
            x,y,r = bomb
            answer = 0
            answer += bfs(x,y,r,i)
            # print(answer)
            maximum_answer = max(maximum_answer, answer)
        return maximum_answer
        
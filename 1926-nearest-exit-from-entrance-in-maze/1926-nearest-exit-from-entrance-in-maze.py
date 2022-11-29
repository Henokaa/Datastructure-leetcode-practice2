class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        inbound = lambda r,c: 0 <= r < len(maze) and 0 <= c < len(maze[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        que = deque()
        level = 0
        que.append(tuple(entrance))
        visited = set()
        visited.add(tuple(entrance))
        while que:
            length = len(que)
            for i in range(length):
                
                temp = que.popleft()
                for x,y in directions:
                    dr = temp[0] + x
                    dc = temp[1] + y
                    # print(maze[dr][dc])
                    if inbound(dr,dc) and maze[dr][dc] == "." and (dr,dc) not in visited:
                        # print((dr,dc))
                        if (not inbound(dr + 1, dc) or not inbound(dr,dc+1) or not inbound(dr-1,dc) or not (inbound(dr,dc-1))):
                            # print(dr,dc, "a")
                            return level + 1
                        else:
                            que.append((dr,dc))
                            visited.add((dr,dc))
                # print(que)
            level += 1
        return -1

                
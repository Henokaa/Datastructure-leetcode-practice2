class Solution:
    def countUnguarded(self, R: int, C: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        state = [[0] * C for _ in range(R)]
        
        GUARD = 1
        WALL = 2
        USED = 3
        
        for x,y in guards:
            state[x][y] = GUARD
        
        for x, y in walls:
            state[x][y] = WALL
            
        for i in range(R):
            current = 0
            for j in range(C):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        
        for i in range(R):
            current = 0
            for j in range(C - 1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        
        
        for j in range(C):
            current = 0
            for i in range(R):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
        
        for j in range(C):
            current = 0
            for i in range(R - 1, -1, -1):
                if state[i][j] == GUARD:
                    current = USED
                elif state[i][j] == WALL:
                    current = 0
                elif state[i][j] == 0:
                    if current == USED:
                        state[i][j] = USED
                        
        count = 0
        for i in range(R):
            for j in range(C):
                if state[i][j] == 0:
                    count += 1
        return count
        
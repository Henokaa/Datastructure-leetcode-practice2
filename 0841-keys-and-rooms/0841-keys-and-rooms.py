class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        def dfs(x):
            for i in range(len(rooms[x])):
                if rooms[x][i] not in visited:
                    visited.add(rooms[x][i])
                    dfs(rooms[x][i])
                    
        
        dfs(0)
    
        return len(visited) == len(rooms)
        
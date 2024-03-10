class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        
        '''
        graph = defaultdict(list)
        ceo = None  # Rename 'root' to something more descriptive
        for i in range(len(manager)):
            if manager[i] == -1:
                ceo = i
                continue
            graph[manager[i]].append(i)  # Corrected edge direction

        visited = set()
        que = deque()
        que.append((ceo, 0))  # Include the time taken to reach the CEO (0 minutes)
        visited.add(ceo)
        total = 0

        while que:
            parent, time_so_far = que.popleft()
            total = max(total, time_so_far)  # Update the maximum time
            for child in graph[parent]:
                if child not in visited:
                    que.append((child, time_so_far + informTime[parent]))
                    visited.add(child)

        return total
                    
            
        
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_size = float('inf')
        
        visited = set()
        for x, y in points:
            visited.add((x,y))
        
        for x1, y1 in points:
            # print(visited, (x1,y1))
            for x2, y2 in visited:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in visited and (x2, y1) in visited:
                        size = abs(x2 - x1) * abs(y2 - y1)
                        # print("size", size)
                        min_size = min(min_size, size)
        
            
        return min_size if min_size != float('inf') else 0
        
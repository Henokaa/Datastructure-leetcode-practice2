class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0,1], [1,0], [-1,0],[0,-1]]
        inbound = lambda r,c: 0 <= r < len(image) and 0 <= c < len(image[0])
        visited = set()
        def dfs(x,y, cur):
            image[x][y] = color
            visited.add((x,y))
            for x1, y1 in directions:
                x2 = x1 + x
                y2 = y1 + y
                if inbound(x2,y2) and (x2,y2) and image[x2][y2] == cur :
                    dfs(x2,y2, cur)
            
        if image[sr][sc] != color:
            dfs(sr,sc, image[sr][sc])
        return image
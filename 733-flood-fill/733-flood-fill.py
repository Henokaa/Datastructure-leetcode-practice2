class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = [[1,0],[0,1], [-1, 0], [0, -1]]
        inbound = lambda r,c: 0<=r<len(image) and 0<=c<len(image[0])
        if image[sr][sc] == newColor:
            return image
        initial = image[sr][sc] 
        def dfs(i,j):
            if image[i][j] == initial:
                image[i][j] = newColor
            for x, y in directions:
                a = i + x
                b = j + y
                if inbound(a,b) and image[a][b] == initial:
                    dfs(a, b)
        dfs(sr, sc)
        return image
        
                                                 
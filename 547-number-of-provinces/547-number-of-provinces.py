class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # parent =[i for i in range(len(isConnected)*len(isConnected))]
        # rank = [1] * len(isConnected)
        # self.size = len(isConnected)
        
        grid = isConnected
        parent = {}
        rank = {}
        direction = [[1,0], [0, 1], [-1, 0], [0, -1]]
        parent = [i for i in range(len(grid))]
        
        print(parent)            
        def findset(x):
            if x == parent[x]:
                return x
            parent[x] = findset(parent[x])
            return parent[x]
        
        def union(x,y):
            x = findset(x)
            y = findset(y)
            
            if x != y:
                parent[y] = x
                   # why not rank of y
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                    union(i,j)
                    
                    
            
        
        count = {}
        maxcount = 0
        for i in parent:
            x = findset(i)
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
                
            maxcount = max(maxcount, count[x])
                    
        
        return len(count)
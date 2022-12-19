class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.parents = [-1 for i in range(n)]
        
        def find(node):
            if self.parents[node] < 0:
                return node
            
            root = find(self.parents[node])
            self.parents[node] = root
            return root
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return 
            
            if abs(self.parents[root1]) > abs(self.parents[root2]):
                self.parents[root1] += self.parents[root2]
                self.parents[root2] = root1
            else:
                self.parents[root2] += self.parents[root1]
                self.parents[root1] = root2
        
        
        for x,y in edges:
            union(x,y)
        
        sr = find(source)
        dc = find(destination)
        
        if sr == dc:
            return True
        else:
            return False
        
        
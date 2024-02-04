class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        union find
        
        self.parents = []
        -ve parents
        +ve references
        
        '''
        self.parent = [-1 for i in range(len(edges)+1)]
        def find(node):
            if self.parent[node] < 0:
                return node
            
            root = find(self.parent[node])
            self.parent[node] = root
            return root
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return False
            
            if abs(self.parent[root1]) > abs(self.parent[root2]):
                self.parent[root1] += self.parent[root2]
                self.parent[root2] = root1
                return True
            
            else:
                self.parent[root2] += self.parent[root1]
                self.parent[root1] = root2
                return True
                
        for x,y in edges:
            if not union(x,y):
                return [x,y]
            
        
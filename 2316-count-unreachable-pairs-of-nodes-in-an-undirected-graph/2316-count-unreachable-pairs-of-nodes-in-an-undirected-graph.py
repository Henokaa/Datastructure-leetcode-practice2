class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
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
            
            
        count = {}
        for i in range(n):
            node = find(i)
            if node in count:
                count[node] += 1
            else:
                count[node] = 1
        ans = 0
        for x,y in count.items():
            ans += y * (n - y)
        
        return ans // 2
            
        
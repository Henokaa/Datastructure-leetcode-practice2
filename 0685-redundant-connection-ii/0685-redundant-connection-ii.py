class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        incomingEdge = collections.defaultdict(list)
        parents = [i for i in range (len(edges)+1)]
        #Find algorithm to find the parent of a node
        def find(n1):
            p = parents[n1]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p
        
        #union algorithm to check if they can be united, if so unite or return False
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2: 
                return False
            parents[p2] = p1
            return True
        
        #unionFind being called to check if there is any cycle in the graph
        # return -1 if there are no cycles in the graph
        def unionFind(edges):
            for n1,n2 in edges:
                if union(n1,n2) == False:
                    return [n1,n2]
            return -1
        # Get the incoming edges and check if there is any node with 2 incoming edges
        # if so remove the last edge and check if it resolves the cycle if not the other edge is the answer
        for n1,n2 in edges:
            incomingEdge[n2].append(n1)
        
        for node in incomingEdge:
            if len(incomingEdge[node])>1:
                edge1 = [incomingEdge[node][0],node]
                edge2 = [incomingEdge[node][1],node]
                # print(edge1,edge2)
                edges.remove(edge2)
                temp = unionFind(edges)
                # print(temp)
                if temp == -1:
                    # when this is out if there is cycle, the ans is the other one
                    return edge2
                return edge1
        return unionFind(edges)
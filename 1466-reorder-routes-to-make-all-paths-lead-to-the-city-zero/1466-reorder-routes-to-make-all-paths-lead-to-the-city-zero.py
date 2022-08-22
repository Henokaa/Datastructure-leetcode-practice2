class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        
        undirected_graph = defaultdict(list)
        actual_graph = defaultdict(set)  # for faster lookup

        for a,b in connections:
            undirected_graph[a].append(b) #Figure out which cities are connected to each other (i.e a road exists between the two) 
            undirected_graph[b].append(a)
            actual_graph[a].add(b)  #Figure out which cities have "valid" roads (i.e you are allowed to go from a to b)

        queue = [(node, 0) for node in undirected_graph[0]] #All neighbours of 0 #(node, destination_node) 
        res = 0
        visited = set([0])# Mark 0 as visited
        
        while queue:
            node, prev = queue.pop()  # destination node parent or prev node
            visited.add(node) #Mark node as visited 

            if not (prev in actual_graph[node]):   #If there is no "valid" road which lets you travel from node to destination_node, you'll have to reverse the road
                res += 1

            for neighb in undirected_graph[node]: #For all unvisited neighbours, you'll have to continue exploring
                if neighb not in visited:
                    queue.append((neighb, node))
        
        return res
        
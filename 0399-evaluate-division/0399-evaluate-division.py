class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = []
        # Get all the nodes and assign them numbers
        for a, b in equations:
            if a not in nodes:
                nodes.append(a)
            
            if b not in nodes:
                nodes.append(b)
        
        charMap = {}

        for i, char in enumerate(nodes):
            # charMap[i]=char
            charMap[char] = i
        
        # create a graph
        graph = defaultdict(list)

        for (a,b), d in zip(equations, values):
            graph[charMap[a]].append((charMap[b], d))
            graph[charMap[b]].append((charMap[a], 1/d))

        n = len(nodes)

        def spf(a,b):
            # Do char translation
            num, den = charMap.get(a, 'notFound'), charMap.get(b, 'notFound') # Numerator and denominator
            if num == 'notFound' or den == 'notFound':
                return float(-1)

            visited = [False]*n
            dist = [float("inf")]*n
            dist[num] = 1
            q = [(0, 1,num)]
            heapq.heapify(q)
            
            while q:
                stops, dis, node = heapq.heappop(q)
                if visited[node]:
                    continue
                
                visited[node] = True
                if node == den:
                    return dist[node]
                
                nbs = graph[node]

                for nb, d in nbs:
                    new_d = d*dis
                    if nb == den: return new_d
                    if not visited[nb] and new_d < dist[nb]:
                        dist[nb] = new_d
                        heapq.heappush(q, (stops+1, new_d, nb))
            
            return float(-1)
        

        return [spf(q1,q2) for q1, q2 in queries]
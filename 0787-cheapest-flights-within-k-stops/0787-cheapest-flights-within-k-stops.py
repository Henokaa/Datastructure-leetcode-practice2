class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # Use a priority queue to keep track of cities with the smallest cost
        # Each element in the queue is a tuple (cost, city, number of stops)
        queue = [(0, src, k+1)]

        # Dictionary to store the minimum cost to reach a city
        min_cost = {src: 0}

        while queue:
            cost, city, stops = heapq.heappop(queue)
            if city == dst:
                return cost
            if stops > 0:
                for v, w in graph[city]:
                    # If we can reach the city with less cost, then only consider this route
                    if cost + w < min_cost.get((v, stops), float('inf')):
                        min_cost[(v, stops)] = cost + w
                        heapq.heappush(queue, (cost+w, v, stops-1))

        return -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
            
        
        minHeap = [(0, k)]
        visited = set()
        count = 0
        while minHeap:
            w1, n1= heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
            count = w1
        return count if len(visited) == n else -1
        '''
        [[1,2,4],[1,3,1],[3,4,1]]
            4
            1
            
            test case i didn't undertand
        '''
        # O(E * logV)
        
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.ans = []
        def dfs(cur, prev):
            self.ans.append(cur)
            for x in edges[cur]:
                if x != prev:
                    dfs(x, cur)
        edges = defaultdict(list)
        for x,y in adjacentPairs:
            edges[x].append(y)
            edges[y].append(x)
        
        for i in edges:
            if len(edges[i]) == 1:
                cur = i
                break
        dfs(cur, float('inf'))
        return self.ans
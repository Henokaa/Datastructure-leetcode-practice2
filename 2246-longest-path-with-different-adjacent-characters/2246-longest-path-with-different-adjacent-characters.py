class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] == -1:
                root = i
            else:
                tree[parent[i]].append(i)
            
        def dfs(root, prev):
            total = []
            twomax = 0
            big = 0
            for i in range(len(tree[root])):
                output = dfs(tree[root][i], s[root])
                # print(output)
                heapq.heappush(total, -output)
                big = max(big, output)
            
            if len(total) >= 2:
                for _ in range(2):
                    value = heapq.heappop(total)
                    twomax += value
            else:
                if len(total) == 1:
                    twomax = total[0]
            
            self.mx = max(self.mx, -twomax + 1)
            # print(root, total)
            rt = 0
            if s[root] != prev:
                rt = max(rt, big + 1)
            # print(root, rt, prev)
            return rt
        

        self.mx = float('-inf')
        dfs(root, "")
        return self.mx
                
        
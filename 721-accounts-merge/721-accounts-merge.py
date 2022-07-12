class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        ans = []
        visited = set()
        self.temp = set()
        a = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                if j == 0:
                    continue
                graph[accounts[i][j]].append(i)
        def dfs(i, accounts):
            
            visited.add(i)
            for j in range(len(accounts[i])):
                if j == 0:
                    continue
                self.temp.add(accounts[i][j])
                for x in graph[accounts[i][j]]:
                    if x not in visited:
                        dfs(x, accounts)
                
        
        for i in range(len(accounts)):
            name = accounts[i][0]
            if i not in visited:
                dfs(i,accounts)
                ans.append([name] + sorted(self.temp))
                self.temp.clear()
        
        return ans
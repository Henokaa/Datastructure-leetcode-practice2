class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = []
        
        for x,y in richer:
            graph[y].append(x)
        memo = {}
        def dfs(x):
            if (quiet[x],x) in memo:
                return memo[(quiet[x],x)]
            minn = (float('INF'), -1)
            for child in graph[x]:
                minn = min(minn, dfs(child)) 
            memo[(quiet[x],x)] =  min(minn, (quiet[x], x))
            
            return memo[(quiet[x],x)] 
        for i in range(len(quiet)):
            answer.append(dfs(i)[1])
        return answer
        
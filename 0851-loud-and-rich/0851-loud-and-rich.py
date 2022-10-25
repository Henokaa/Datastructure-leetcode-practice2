class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        '''
        
        '''
        # Do the graph
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        memo = {}
        # dfs through the graph
        def dfs(i):
            if (quiet[i],i) in memo:
                return memo[(quiet[i],i)]
            
            mini = (float('inf'),-1) 
            for child in graph[i]:
                temp1 = dfs(child)
                mini = min(mini, (temp1[0], temp1[1]))
                
            mini = min(mini, (quiet[i], i))
            memo[(quiet[i],i)] = mini
            return mini
        
        answer = []
        for i in range(len(quiet)):
            # temp2 = dfs(i)
            answer.append(dfs(i)[1])
            
        return answer
       
        
        
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        '''
         0
        [1,0,0,0,0,7,7,5]
        
        graph[1] = 0 
        '''
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i]].append(i)
        
        print(graph)
        
        
        max_answer = float(-inf)
        answer = None
        for x,y in graph.items():
            total = sum(y)
            # print(x, max_answer, total)
            if total == max_answer:
                if answer and answer > x:
                    answer = x
            if total > max_answer:
                max_answer = max(max_answer, sum(y))
                answer = x
            
        return answer
            
        
        
                    
        
        
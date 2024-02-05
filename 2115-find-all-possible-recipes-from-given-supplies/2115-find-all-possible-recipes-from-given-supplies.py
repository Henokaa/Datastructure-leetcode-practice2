class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
        que = [supplies]
        
        graph["yeast"] = "bread"
        indegree["bread"] += 1
        
        '''
        graph = defaultdict(list)
        indegree = defaultdict(int)
        que = deque()
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] += 1
            
        for x in supplies:
            que.append(x)
        answer = []
        while que:
            output = que.popleft()
            for child in graph[output]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)
                    answer.append(child)
                
        return answer
                    
                
            
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        checkrec = set(recipes)
        checksup = set(supplies)
        indegree = {}
        # print(checkrec)
        graph = defaultdict(list)
        for i in range(len(recipes)):
            indegree[i] = 0
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in checkrec:
                    index = recipes.index(ingredients[i][j])
                    graph[index].append(i)
                    indegree[i] += 1
        
        # print(graph)
        # print(indegree)
        que = deque()
        visited = set()
        valid = set()
        for x,y in indegree.items():
            if y == 0:
                flag = 0
                for item in ingredients[x]:
                    if item not in checksup:
                        flag = 1
                if flag == 0:
                    que.append(x)
                    visited.add(x)
                    valid.add(recipes[x])

        ans = set()
        # print(que)
        while que:
            food = que.popleft()
            flag = 0
            for x in ingredients[food]:
                if x in checksup or x in valid:
                    continue
                else:
                    flag = 1
            if flag == 0:
                ans.add(recipes[food])
                valid.add(recipes[food])
                for child in graph[food]:
                    if child not in visited:
                        que.append(child)
                        # valid.add(recipes[child])
                        visited.add(child)
                        

#         for i in range(len(recipes)):
#             if recipes[i] not in ans:
#                 flag = 0
#                 for x in range(len(ingredients[i])):
#                     if ingredients[i][x] not in checksup or ingredients[i][x] not in checkrec:
#                         flag = 1
                        
#                 if flag == 0:
#                     ans.append(recipes[i])
        return list(ans)
                
                    
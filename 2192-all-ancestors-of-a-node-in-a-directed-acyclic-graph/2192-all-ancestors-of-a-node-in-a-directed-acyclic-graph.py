class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        parent = defaultdict(list)
        child = defaultdict(list)
        ancestor = {}
        indegree = {}
        
        for i in range(n):
            ancestor[i] = []
            indegree[i] = 0
            
        for x,y in edges:
            child[x].append(y)
            parent[y].append(x)
            indegree[y] += 1
            
        que = deque()
        visited = set()
        for i in indegree:
            if indegree[i] == 0:
                que.append(i)
                visited.add(i)
        # print(que)
        
        while que:
            temp = que.popleft()
            
            for childs in child[temp]:
                tempparent = []
                if childs not in visited:
                    flag = 0
                    for pars in parent[childs]:
                        if pars not in visited:
                            flag = 1
                    if flag == 0:
                        for par in parent[childs]:
                            tempparent.append(par)
                            for x in ancestor[par]:
                                tempparent.append(x)
                        tempparent = set(tempparent)
                        ancestor[childs] = sorted(tempparent)
                        que.append(childs)
                        visited.add(childs)
                    else:
                        que.append(childs)
        
        ans = []
        for i in range(n):
            ans.append(ancestor[i])
        
        return ans
       
        
                    
                    
                    
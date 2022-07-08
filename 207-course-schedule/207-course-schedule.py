from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        indegree={}
        v = numCourses
        a = prerequisites
        for i in range(v):
            graph[i]=[]
            indegree[i]=0
        # {0: 0, 1: 0}
        # print(indegree)
        for edge in a:
            parent=edge[0]
            child=edge[1]
            indegree[child]+=1
            graph[parent].append(child)
        # print(indegree) this is like incoming
        # {0: 1, 1: 0}
        # print(graph) childs
        # {0: [1], 1: []} 
        sources=deque()
        for i,j in indegree.items():
            if(j==0):
                sources.append(i)
        # print(sources)
        # deque([0])
        ans=[]
        while sources:
            c=sources.popleft()
            ans.append(c)
            for nbr in graph[c]: # graph[0] - [1] the nodes 
                indegree[nbr]-=1 # indegree with number in 1 there was one incomming decrease
                if(indegree[nbr]==0):
                    sources.append(nbr)
        if(len(ans)==v):
            return True
        return False
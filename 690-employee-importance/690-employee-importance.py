"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ''' id: childs'''
        graph = defaultdict(list)
        self.imp = 0
        for i in range(len(employees)):
            graph[employees[i].id] = employees[i] 
        
        def dfs(graph, i):
            self.imp += graph[i].importance
            
            for j in graph[i].subordinates:
                dfs(graph, j)
            
        
        dfs(graph, id)
        return self.imp
        



































































































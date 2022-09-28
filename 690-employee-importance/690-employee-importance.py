"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

'''
id : emp[0]
'''

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ''' id: childs'''
        emps = {}
        for emp in employees:
            emps[emp.id] = {"imp": emp.importance, "subs": emp.subordinates}
        
    
    
        
        def dfs(employee):
            for sub in emps[employee]['subs']:
                emps[employee]['imp'] += dfs(sub)
            return emps[employee]['imp']
                
        return dfs(id)
    
        



































































































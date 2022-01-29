

Success
Details 
Runtime: 260 ms, faster than 15.97% of Python3 online submissions for Employee Importance.
Memory Usage: 15.6 MB, less than 70.96% of Python3 online submissions for Employee Importance.


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
        employeeMap = { e.id: e for e in employees}
        def dfs(eid):
            employee = employeeMap[eid]
            return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
        
        return dfs(id)

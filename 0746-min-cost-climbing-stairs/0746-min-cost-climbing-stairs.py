class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        costs = [10,15,20]
        
        10,15,20, _
        
        clarrify
        
            dfs()
                [pos, cos]
        constraint 
        
        approach 
        
        edgecase
        
        '''
        answer = float('inf')
        memo = {}
        def dfs(i):
            
            if i in memo:
                return memo[i]
            
            nonlocal answer
            if i == len(cost):
                return 0
            
            if i > len(cost):
                return 0
            
            one = cost[i] + dfs(i + 1)
            two = cost[i] + dfs(i + 2)
            
            memo[i] = min(one, two)
            
            return memo[i]
        
        
        
        
        return min(dfs(0), dfs(1))
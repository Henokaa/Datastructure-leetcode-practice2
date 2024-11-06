class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        clarrify
        
        
        constraint 
        
        
        approach 
            [1,100,1,1,1,100,1,1,100,1]
        
        edgecase
        
        
        '''
        
        array = [0] * len(cost)
        
        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        array[-1] = cost[-1]
        array[-2] = cost[-2]
        
        p1 = len(cost) - 3
        
        while p1 >= 0:
            cost[p1] = cost[p1] + min(cost[p1 + 1], cost[p1 + 2])
            # print(array)
            p1 -= 1
        
        return min(cost[0], cost[1])
        
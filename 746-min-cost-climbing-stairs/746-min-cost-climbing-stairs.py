class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''[10, 15, 20]'''
        length = len(cost)
        
        a = len(cost) - 1
        b = len(cost) - 2
        c = length - 3
        
        while c >= 0:
            temp = min(cost[a],cost[b])
            
            cost[c] = cost[c] + temp
            c -= 1
            a -= 1
            b -= 1
        return min(cost[0], cost[1])
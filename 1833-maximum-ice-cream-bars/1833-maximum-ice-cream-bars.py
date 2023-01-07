class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n, icecreams = len(costs), 0
        m = max(costs)

        costsFrequency = [0] * (m + 1)
        for cost in costs:
            costsFrequency[cost] += 1
        
        # print(costsFrequency)
        
        
        for cost in range(1, m + 1):
            # No ice cream is present costing 'cost'.
            if costsFrequency[cost] == 0:
                continue
            if cost > coins:
                break
            
            temp = cost * costsFrequency[cost]
            if temp <= coins:
                coins -= temp
                icecreams += costsFrequency[cost]
            else:
                take = coins // cost 
                icecreams += take
                break
            
            
            
        return icecreams
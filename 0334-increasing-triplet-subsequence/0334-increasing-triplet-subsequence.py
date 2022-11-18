class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 10 ** 20
        
        s1 = INF
        s2 = INF
        
        for x in nums:
            # print(x, s1,s2)
            if x > s2:
                return True
            if x > s1:
                s2 = min(x, s2)
            s1 = min(x, s1)
        return False
            
        
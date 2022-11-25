from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        sub = []
        for num in nums:
            pos = bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
                
            if len(sub) >= 3:
                return True
        return False
            
        
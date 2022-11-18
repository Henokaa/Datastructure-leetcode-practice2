from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val <= sub[mid]:
                    hi = mid - 1
                
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            # because for rg 3 its one
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
            
            # print(val , pos, sub)
        return len(sub)
        
                
            
                
            
    
        



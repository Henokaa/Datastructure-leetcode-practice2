class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,1,1,1] h = 4  k= 11  (min)
        # [2,2,2,2]  h = 8  k=5.5
        r = max(piles) 
        l = 1
        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for i in piles:
                div = i / mid
                time += math.ceil(div)
                
            if time <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return r + 1
    # [1,2,2,3]
    '''
    The most important rule in binary search 
 L = -1 and r = len(nums), this only works for index, and not for like a question koko eating banana. 
 l = mid
 r = mid
 
 but for l <= r where l = 0, r = len(nums) - 1 
 l = mid + 1
 r = mid - 1
    '''
            
                
        
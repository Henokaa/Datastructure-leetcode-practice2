import random
class Solution:
    def __init__(self, w: List[int]):
        '''
        [1, 4, 6]
        r = 2
        if not r <= nums[mid]:
            l = mid + 1
    
        '''
        self.w = []
        total = 0
        for weight in w:
            total += weight
            self.w.append(total)
        self.total = total
        
        
    def pickIndex(self) -> int:
        ran= random.randint(1, self.total)
        '''
        [1, 3]
        [1, 4, 6]
        
        '''
        answer = float('inf')
        left = 0
        right = len(self.w) - 1
        while left <= right:
            mid = left + (right - left) //2
            if ran <= self.w[mid]:
                answer = mid 
                right = mid - 1
            elif ran > self.w[mid]:
                left = mid + 1
        return answer

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
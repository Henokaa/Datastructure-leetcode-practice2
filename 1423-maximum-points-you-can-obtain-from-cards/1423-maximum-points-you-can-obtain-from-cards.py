class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [1,2,3,4,5,6,1]
         ^
        
        k = 3
        '''
        r = 0
        total = 0
        while r < k:
            total += cardPoints[r]
            r += 1
        r -= 1
        # r -= 1
        # print(total)
        mx = float('-INF')
        mx = max(mx, total)
        l = len(cardPoints) - 1
        # total - nums[r-i] + nums[len(s) - i]
        for i in range(1, k + 1):
            total = total - cardPoints[r] + cardPoints[l]
            r -= 1
            l -= 1
            mx = max(mx, total)
        return mx
            
            
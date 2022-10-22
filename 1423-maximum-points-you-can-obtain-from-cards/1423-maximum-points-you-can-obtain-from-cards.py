class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [10, 1, 2, 4, 5, 4, 3]
        [10, 11,13,17,22,26,29]
        [29, 19,18,16,12, 7, 3]
         ^              
                             ^
        
        k = 3
        '''
        leftmost = 0
        leftprefix = []
        # making leftprefix
        for i in cardPoints:
            leftmost += i
            leftprefix.append(leftmost)
        
            
        rightmost = 0
        rightprefix = []
        # make the rightprefix
        for i in cardPoints[::-1]:
            rightmost += i
            rightprefix.append(rightmost)
       
        rightprefix = rightprefix[::-1]
        # do the calculation
        mx = float('-INF')
        mx = max(mx, rightprefix[len(cardPoints) - k])
        K = k -1
        for i in range(k):
            temp1 = K - i
            temp2 = (len(cardPoints)) - (K - temp1)
            if temp2 == len(cardPoints):
                mx = max(mx, leftprefix[temp1])
                continue
            # print(leftprefix[temp1], rightprefix[temp2])
            mx = max(mx, leftprefix[temp1] + rightprefix[temp2])
            
        return mx
            
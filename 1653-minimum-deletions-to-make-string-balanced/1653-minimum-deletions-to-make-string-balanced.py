class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt = 0
        arrB = [0] * len(s)
        for i in range(len(s)):
            arrB[i] = cnt
            if s[i] == 'b':
                cnt += 1
    
        cnt = 0
        arrA = [0] * len(s)
        for i in range(len(s)-1, -1, -1):
            arrA[i] = cnt
            if s[i] == 'a':
                cnt += 1
        ans = len(s)
        for i in range(len(s)):
            ans = min(ans,arrA[i] + arrB[i])
    
        return ans
        
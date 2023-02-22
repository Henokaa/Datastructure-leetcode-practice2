class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0

        while '01' in s:
            ans += 1
            s = s.replace('01', '10')
            
        return ans
        
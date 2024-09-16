class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        saved_string = set()
        saved_string.add(s[l])
        answer = float('-inf')
        while r < len(s):
            if s[r] not in saved_string:
                saved_string.add(s[r])
                r += 1
            else:
                while s[r] in saved_string:
                    saved_string.remove(s[l])
                    l += 1
                
                saved_string.add(s[r])
                r += 1
                
            answer = max(answer, len(saved_string))
        
        return answer
        
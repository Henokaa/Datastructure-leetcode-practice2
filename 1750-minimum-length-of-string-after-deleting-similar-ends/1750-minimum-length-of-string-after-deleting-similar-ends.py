class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        
        while l < r:
            if s[l] == s[r]:
                char = s[l]
                while l <= r and char == s[l]:
                    l += 1
                
                char = s[r]
                while l <= r and char == s[r]:
                    r -= 1
            else:
                break
            
            
        # print("ANS", (l,r))
        return r - l + 1 if l <= r else 0
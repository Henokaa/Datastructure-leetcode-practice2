class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = 0 
        r = 0
        res = 0
        maxres = 0
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                res = r - l + 1
                maxres = max(res, maxres)
                r += 1
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
        return maxres
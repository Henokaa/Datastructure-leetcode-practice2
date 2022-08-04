class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            cur = 0
            if 1 <= int(s[i]) <= 9:
                cur += dfs(i+1)
            if 10 <= int(s[i:i+2]) <= 26 and len(s[i:i+2]) == 2:
                cur += dfs(i+2)
            return cur
        return dfs(0)
            
                
        
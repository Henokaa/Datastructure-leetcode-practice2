class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i > len(s) - 1:
                return 1
            # print(i)
            
            first = s[i:i+1]
            l = 0
            if len(first) == 1 and first[0] != "0" and 1 <= int(first) <= 26:
                l = dfs(i + 1)
            sec = s[i:i+2]
            r = 0
            if len(sec) == 2 and sec[0] != "0" and 1 <= int(sec) <= 26:
                r = dfs(i + 2)
            
            return l + r
        
        return dfs(0)
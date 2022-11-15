class Solution:
    def numSplits(self, s: str) -> int:
        visited = set()
        r = 0
        count = 0
        prefix1 = []
        while r < len(s):
            if s[r] not in visited:
                count += 1
                visited.add(s[r])
            prefix1.append(count)
            r += 1
        
        visited = set()
        prefix2 = []
        r = len(s) - 1
        count = 0
        while r >= 0:
            if s[r] not in visited:
                count += 1
                visited.add(s[r])
            prefix2.append(count)
            r -= 1
        
        prefix2 = prefix2[::-1]
        
        print(prefix1, prefix2)
        
        ans = 0
        for i in range(len(s)-1):
            if prefix1[i] == prefix2[i+1]:
                ans += 1
                
        return ans
            
        
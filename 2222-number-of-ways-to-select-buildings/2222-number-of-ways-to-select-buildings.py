class Solution:
    def numberOfWays(self, s: str) -> int:
        N = len(s)
        total = 0
        seen = [[0] * 2 for _ in range(2)]
        
        for i in range(N):
            current = int(s[i])
            
            total += seen[1][1 - current]
            seen[1][current] += seen[0][1-current]
            seen[0][current] += 1
        return total
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        
        f = collections.defaultdict(lambda: set())
        
        for i, x in logs:
            f[i].add(x)
        
        for i in f.keys():
            ans[len(f[i]) - 1] += 1
        
        return ans
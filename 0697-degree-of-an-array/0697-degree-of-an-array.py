class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        m = max([ len(v) for v in d.values() ])
        best = len(nums)
        for v in d.values():
            if len(v)==m:
                best = min(best,v[-1]-v[0]+1)
        return best
        
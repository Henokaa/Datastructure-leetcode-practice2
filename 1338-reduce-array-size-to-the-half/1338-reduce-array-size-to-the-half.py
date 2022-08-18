class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        counts = sorted(counts.values(), reverse = True)
        l = 0
        mid = 0
        while l < len(arr):
            if mid >= len(arr)//2:
                break
            mid += counts[l]
            l += 1
        
        return l
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        extra = []
        for i in range(len(capacity)):
            extra.append(capacity[i] - rocks[i])
        
        extra.sort()
        r = 0
        total = 0
        ans = 0
        while r < len(extra):
            total += extra[r]
            if total <= additionalRocks:
                ans = r + 1
            else:
                break
            r += 1
        return ans
        
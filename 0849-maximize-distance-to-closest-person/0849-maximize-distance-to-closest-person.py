class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        forward = []
        total = float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                total = 0
            forward.append(total)
            total += 1
        # print(forward)
        
        backward = []
        total = float('inf')
        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1:
                total = 0
            backward.append(total)
            total += 1
        
        backward = backward[::-1]
        # print(backward)
        l = 0
        r = 0
        ans = 0
        while r < len(backward):
            small = min(forward[l], backward[r])
            ans = max(ans, small)
            l += 1
            r += 1
        return ans
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = 0
        n = [0] * 60

        for i in time:
            n[i%60]+=1

        for i in range(0, 31):
            if n[i] == 0:
                continue
            if (i == 0 or i == 30):
                if n[i] > 1:
                    c+=(n[i]*(n[i]-1)/2)
            else:
                 c+=(n[i]*n[60-i])
        return int(c)
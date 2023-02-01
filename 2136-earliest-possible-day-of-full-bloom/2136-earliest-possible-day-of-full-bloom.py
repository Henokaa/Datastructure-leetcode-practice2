class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        l=[]
        for i in range(len(plantTime)):
            l.append((plantTime[i],growTime[i]))
        l.sort(key=lambda pair: pair[1])
        mx_day=0
        c_sum=0
        for i in range(len(plantTime)-1,-1,-1):
            c_sum+=l[i][0]
            mx_day=max(mx_day,c_sum+l[i][1])
        return mx_day
        
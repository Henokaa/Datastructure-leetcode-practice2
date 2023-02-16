class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        n = len(changed) // 2
        counter = collections.Counter(changed)
        doubles = 0
        res = []
        for num in sorted(counter):
            count = counter[num]
            if num * 2 in counter:
                if num != num * 2:
                    count = min(count, counter[num*2])
                else:
                    count = counter[num] // 2
                counter[num] -= count
                counter[num* 2] -= count
                for i in range(count):
                    res.append(num)
     
        return res if len(res) == n else []
            
            
            
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
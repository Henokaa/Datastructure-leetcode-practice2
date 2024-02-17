class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq_count = Counter(arr)
        sorted_count = sorted(freq_count.items(), key = lambda x: x[1])
        
        # print(sorted_count)
        count = 0
        for x,y in sorted_count:
            k -= y
            if k < 0:
                break
            count += 1
        
        ans = len(sorted_count) - count 
        return ans
            
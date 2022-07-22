import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for x in range(len(nums)):
            count[nums[x]] = 1 + count.get(nums[x], 0)
            
        for x,y in count.items():
            freq[y].append(x)
        
        res = []
       
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
            
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        dic = {}
        freq = [[] for i in range(len(nums) + 1)]
        ans = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            # count[n] = 1 + count.get(n, 0)
        dic = sorted(count.items(),key = lambda x:x[1],reverse = True)
        # print(dic)
        for x in dic:
            ans.append(x[0])
            if len(ans) == k:
                return ans
#         for n, c in count.items():
#             freq[c].append(n)
        
#         print(count)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        
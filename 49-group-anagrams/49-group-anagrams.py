class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # diction = {}
        # ans = []
        # for i in range(len(strs)):
        #     a = sorted(strs[i])
        #     for x,y in diction.items():
        #         if x == a:
        #             ans[y].append(x)
        #         else:
        #             ans.append([a])
        #             diction[a] = y
        #     print()
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()
                 
        
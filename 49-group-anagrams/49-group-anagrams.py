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
        for i in strs:
            count = [0] * 26
            for j in i:
                x = ord(j) - ord("a") 
                count[x] += 1
            res[tuple(count)].append(i)
        return res.values()
    
    # time complexity => 0(n * m * 26)
                 
        
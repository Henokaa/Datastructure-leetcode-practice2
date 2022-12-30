class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        saved = {}
        for x,y in items1:
            saved[x] = y

        for x,y in items2:
            if x in saved:
                saved[x] += y
            else:
                saved[x] = y
        
        diction = sorted(saved.items(),key = lambda x:x[0])
        ans = []
        for x,y in diction:
            ans.append([x,y])
        return ans
        
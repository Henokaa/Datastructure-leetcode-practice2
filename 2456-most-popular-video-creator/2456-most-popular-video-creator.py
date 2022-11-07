class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        '''
        alice : [(one,5) 
        
        '''
        total = defaultdict(int)
        saved = {}
        mx = float('-inf')
        for creator, i, view in zip(creators, ids, views):
            total[creator] += view
            if creator not in saved:
                saved[creator] = (i, view)
            else:
                if view > saved[creator][1]:
                    saved[creator] = (i, view)
                elif view == saved[creator][1] and i < saved[creator][0]:
                    saved[creator] = (i, view)
                    
        mx = max(total.values())
        ans = []
        for x in total.keys():
            if total[x] == mx:
                ans.append([x,saved[x][0]])
                
        return ans
        
            
                    
            
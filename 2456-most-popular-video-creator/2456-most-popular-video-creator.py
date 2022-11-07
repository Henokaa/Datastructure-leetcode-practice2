class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        '''
        alice : [0,2
        
        ids: [
        
        one: 5
        
        '''
        name = defaultdict(list)
        vw = defaultdict(int)
        for i in range(len(views)):
            if creators[i] in name:
                for elements in name[creators[i]]:
                    if views[i] > views[elements]:
                        name[creators[i]] = []
                        name[creators[i]].append(i)
                        break
                    elif views[i] == views[elements]:
                        name[creators[i]].append(i)
                        break
                    else:
                        break
            else:
                name[creators[i]].append(i) 
                
        # print(name)
        
        
        mx = float('-inf')
        for i in range(len(views)):
            vw[creators[i]] += views[i]
            mx = max(mx, vw[creators[i]])
        # print(mx)
        
        
        ans = []
        temp = []
        for x,y in vw.items():
            if y == mx:
                for ele in name[x]:
                    temp.append(ids[ele])
                names = sorted(temp)
                ans.append([x, names[0]])
                temp = []
            
        return ans
        
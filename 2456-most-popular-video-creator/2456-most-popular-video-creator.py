class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        '''
        x,y,z
        
        alice = one, 5
        bob = two, 5
        
        alice = 10
        bob = 10
        
        alice = 
        '''
        
        name = {}
        values = {}
        maximum = 0
        for creators, ids, views in zip(creators, ids, views):
            if creators in name:
                if views >= name[creators][1]:
                    if views == name[creators][1]:
                        if name[creators][0] > ids:
                            name[creators] = (ids, views)
                    else:
                        name[creators] = (ids, views)
            else:
                name[creators] = (ids, views)
                
            if creators in values:
                values[creators] += views
                maximum = max(maximum, values[creators])
            else:
                values[creators] = views
                maximum = max(maximum, values[creators])
        
        answer = []
        for key, result in values.items():
            if result == maximum:
                answer.append([key ,name[key][0]])
            
        return answer
        
        
            
            
            
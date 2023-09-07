class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # first element dictionary
        # subtracting two dict
        
        '''
        c = 1
        o = 2
        l = 1
        '''
        element = defaultdict(int)
        ans = defaultdict(int)
        for i in words[0]:
            ans[i] += 1

        # print(answer)
        for i in range(len(words)):
            for x in words[i]:
                element[x] += 1
            
            for x,y in element.items():
                if x in ans:
                    ans[x] = min(ans[x], y)
            
            delete = set()
            for x,y in ans.items():
                if x not in element:
                    delete.add(x)
            
            for x in delete:
                del ans[x]
            element = defaultdict(int)
            
        answer = []
        for x, y in ans.items():
            for i in range(y):
                answer.append(x)
            
       
        return answer
                
            
                    
                
                
            
                
        
        
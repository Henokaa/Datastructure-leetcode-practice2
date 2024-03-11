class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        
        '''
        letters = Counter(s)
        # print(letters)
        ans = ""
        visited = set()
        for i in range(len(order)):
            if order[i] not in visited and order[i] in letters:
                ans += order[i] * letters[order[i]]
                visited.add(order[i])
            
        for i in s:
            if i not in visited:
                ans += i
    
        return ans
                             
        
                             
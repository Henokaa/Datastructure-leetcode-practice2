class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in word:
                word[i] += 1
            else:
                word[i] = 1
        
        
        for x in t:
            if x in word:
                word[x] -= 1
                if word[x] == -1:
                    return False
            else:
                return False
            
        return True
                
                
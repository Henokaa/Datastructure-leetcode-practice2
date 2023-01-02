class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        flag = 0
        for i in range(len(word)):
            if ord('A') <= ord(word[i]) <= ord('Z'):
                if i == 0:
                    flag = 1
                capital += 1
        
        if (capital == 1 and flag == 1) or capital == len(word) or capital == 0:
            
            return True
        return False
                
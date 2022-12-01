class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        pass
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        
        size = len(s)//2
        first = s[:size]
        sec = s[size:]
        print(first, sec)
        c1 = 0
        c2 = 0
        for i in first:
            if i.lower() in vowels:
                c1 += 1
        
        for i in sec:
            if i.lower() in vowels:
                c2 += 1
        return c1 == c2
                
                
        
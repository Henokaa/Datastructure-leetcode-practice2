class Solution:
    def countSubstrings(self, s: str) -> int:
        ''' Brute force - our sliding window(substring) for every element o(n^2) to check if it palindrom o(n^3)'''
        res = 0
        
        for i in range(len(s)):
            l , r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
     
                
        return res
        
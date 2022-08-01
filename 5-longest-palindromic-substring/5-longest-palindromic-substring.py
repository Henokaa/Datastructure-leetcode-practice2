class Solution:
    def longestPalindrome(self, s: str) -> str:
        ''' taking each character n,  expanding in each character n. so o(n^2)'''
        res = 0
        ans = ""
        for i in range(len(s)):
            l , r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if (r-l+1) > res:
                    ans = s[l:r+1]
                    res = r-l + 1
                
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > res:
                    ans = s[l:r+1]
                    res = r-l + 1
                l -= 1
                r += 1
     
                
        return ans
                
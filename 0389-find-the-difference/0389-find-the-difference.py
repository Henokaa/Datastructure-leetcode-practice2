class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters_s = [0] * 26
        for i in s:
            letters_s[ord(i) - ord('a')] += 1
        # print(letters_s, ord('a') + letters_s[0] )
        letters_t = [0] * 26
        for i in t:
            index = ord(i) - ord('a')
            letters_t[index] += 1
        
        for x in range(len(letters_s)):
            if letters_s[x] != letters_t[x]:
                return chr(ord('a') + x )
        
        return ""
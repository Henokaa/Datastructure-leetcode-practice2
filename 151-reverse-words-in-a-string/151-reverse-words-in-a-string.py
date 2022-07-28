class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        
        b = " ".join(i for i in a[::-1])
        return b
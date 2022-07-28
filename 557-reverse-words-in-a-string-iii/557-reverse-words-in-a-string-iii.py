class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        return " ".join(i[::-1] for i in a)
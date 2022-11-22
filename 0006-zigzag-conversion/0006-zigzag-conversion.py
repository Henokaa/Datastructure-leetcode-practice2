class Solution:
    def convert(self, s: str, numRows: int) -> str:
        text = [''] * numRows
        steps = 0
        i = 0
        while i < len(s):
            steps = 0
            while i < len(s) and steps <= numRows-1:
                text[steps] += s[i]
                steps += 1
                i += 1
            
            steps -= 2
            while i < len(s) and steps >= 1:
                text[steps] += s[i]
                steps -= 1
                i += 1
            
        return "".join(text)
        
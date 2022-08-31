class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        ans = [''] * numRows
        
        i, x = 0, 0
        
        while i < len(s):
            if x == 0:
                while x < numRows - 1 and i < len(s):
                    ans[x] += s[i]
                    x += 1
                    i += 1
            if x == numRows - 1:
                while x > 0 and i < len(s):
                    ans[x] += s[i]
                    x -= 1
                    i += 1
            if i >= len(s):
                break
                
        return ''.join(ans)
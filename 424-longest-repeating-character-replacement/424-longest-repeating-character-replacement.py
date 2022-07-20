class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 1
        r = 0
        l = 0
        x = 0
        while r < len(s):
            if x == 0:
                count[s[r]] = 1 + count.get(s[r], 0)
                
            if (r - l + 1) - max(count.values()) <= k: 
                temp = r - l + 1
                print(temp, s[r])
                res = max(temp, res)
                r += 1
                x = 0
            else:
                
                
                count[s[l]] -= 1
                print(count)
                l += 1
                x = 1
            
        return res
                
        
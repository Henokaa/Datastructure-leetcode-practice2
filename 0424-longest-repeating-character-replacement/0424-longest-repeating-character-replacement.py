class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "AABABBA"
         ^
              ^
        '''
        r = 0
        l = 0
        count = defaultdict(int)
        mx = 0
        while r < len(s):
            count[s[r]] += 1
            need = r - l + 1 - max(count.values())
            while need > k:
                count[s[l]] -= 1
                l += 1
                need = r - l + 1 - max(count.values())
                
            if need <= k:
                mx= max(mx, r - l + 1)
                r += 1
                
        return mx
            
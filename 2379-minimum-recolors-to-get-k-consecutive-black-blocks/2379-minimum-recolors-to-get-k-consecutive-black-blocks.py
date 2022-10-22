class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        "WBBWWBBWBW"        k = 7
         ^
               ^
        '''
        #dictionary for the 7 elements
        words = defaultdict(int)
        for i in range(k):
            if blocks[i] in words:
                words[blocks[i]] += 1
            else:
                words[blocks[i]] = 1
        # print(words)
        
        # sliding window
        l = 0
        r = k - 1
        result = float('inf')
        flag = 0
        if r == l:
            flag = 1
        while r <= len(blocks) - 1:
            operations = words['W']
            result = min(result, operations)
            if r == len(blocks) - 1:
                break
            if flag == 1:
                words[blocks[r]] -= 1
                r += 1
                words[blocks[r]] += 1
                continue
            words[blocks[l]] -= 1
            l += 1
            r += 1
            words[blocks[r]] += 1
            
        return result
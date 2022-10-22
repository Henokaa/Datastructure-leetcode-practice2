class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        "WBBWWBBWBW"        k = 7
         ^
               ^
        '''
        #dictionary for the 7 elements
        best = 10 ** 20
        current = 0
        '''
        "WBBWWBBWBW"
                ^
        '''
        N = len(blocks)
        for i in range(N):
            # print(blocks[i], current)
            if blocks[i] == "W":
                current += 1
            if i - k >= 0 and blocks[i-k] == "W":
                current -= 1
            
            if i - k + 1 >= 0:
                best = min(best, current)
        return best
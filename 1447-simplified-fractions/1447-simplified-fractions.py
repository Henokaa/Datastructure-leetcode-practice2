class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        up = 1
        # while up <= n-1
        # up < bottom
        # bottom <= n
        saved = set()
        s = ""
        ans = []
        while up <= n- 1:
            bottom = up + 1
            while bottom <= n:
                if up/bottom not in saved:
                    s += str(up) + "/" + str(bottom)
                    ans.append(s)
                    s = ""
                saved.add(up/bottom)
                    
                bottom += 1
            up += 1
            
        
        return ans
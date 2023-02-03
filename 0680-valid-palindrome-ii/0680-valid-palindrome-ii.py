class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                # try both ways
                l2, r2 = l+1, r
                l3, r3 = l, r-1

                first, second = True, True
                # l+1, r
                while l2 < r2:
                    if s[l2] != s[r2]:
                        first = False
                        break
                    l2 +=1
                    r2 -=1
                # l, r-1
                while l3 < r3:
                    if s[l3] != s[r3]:
                        second = False
                        break
                    l3 +=1
                    r3 -=1
                
                if first or second: # if any of them returns True
                    return True
                else:
                    return False

            l+=1
            r-=1

        return True
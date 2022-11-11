class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        "A man, a plan, a canal: Panama"
          ^
                                     ^

        '''
        def checker(i):
            if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z') or ord('0') <= ord(i) <= ord('9'):
                return True
            else:
                return False
        l = 0
        r = len(s)-1
        if not checker(s[l]):
            while l < len(s) and not checker(s[l]):
                l += 1
        if not checker(s[r]):
            while r >= 0 and not checker(s[r]):
                r -= 1
                
      
        while l < r:
            # if valid 
            if s[l].lower() == s[r].lower():
                # print(s[l], s[r]) 
                l += 1
                r -= 1
                while l < len(s) and not checker(s[l]):
                    l += 1
                while r >= 0 and not checker(s[r]):
                    r -= 1
            else:
                return False
            
        return True
            # l += 1 and r -= 1
            # move l while is not char
            
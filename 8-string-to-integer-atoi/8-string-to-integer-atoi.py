class Solution:
    def myAtoi(self, s: str) -> int:
        
        if s == "":
            return 0
        
        s = s.strip()
        flag = 1
        
        
        if s and s[0] == '-':
            flag = -1
            s = s[1:]
        elif s and s[0] == '+':
            flag = 1
            s = s[1:]
         
        num = 0
        for c in s:
            if c.isdigit():
                num = (num*10)+int(c)
            else:
                break
                
        res = (num*flag)     
        if res>=(2**31):
            return (2**31)-1
        elif res<-(2**31):
            return -(2**31)
        return res
        
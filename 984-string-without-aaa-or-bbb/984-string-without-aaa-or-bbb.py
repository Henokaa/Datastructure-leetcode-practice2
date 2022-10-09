class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        s = ""
        while a or b:
            if len(s)>=2 and s[-1] == s[-2]:
                if s[-1] == "a":
                    s += "b"
                    b -= 1
                else:
                    s += "a"
                    a -= 1
            else:
                if a > b:
                    s += "a"
                    a -= 1
                else:
                    s += "b"
                    b -= 1
        return s

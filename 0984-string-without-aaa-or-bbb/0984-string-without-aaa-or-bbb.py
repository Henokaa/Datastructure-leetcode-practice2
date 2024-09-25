class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        word  = ""
        while b > 0 or a > 0:
    
            if len(word) >= 2 and word[-2:] == "bb":
                word += "a"
                a -= 1
            elif len(word) >= 2 and word[-2:] == "aa":
                word += "b"
                b -= 1
                
            elif b >= a:
                word += "b"
                b -= 1
                
            elif a > b:
                word += "a"
                a -= 1
        
            
                
        return word
            
            
                

        
                
class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while ans//10 != 0:
            num = ans
            ans = 0
            while num:
                rem = num % 10
                ans += rem
                num = num // 10
            
        return ans
            
        
        
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
        r = 0
        total = 0
        while r <= len(s)-1:
            if r >= 1 and roman[s[r-1]] < roman[s[r]]:
                total += roman[s[r]] - roman[s[r-1]] - roman[s[r-1]]
            else:
                total += roman[s[r]]
            r += 1
        return total
        # "LXIV" - 50 + 10 + 1 + 5 - 1 - s[r-1] 
        # "IV" - 1 + 4
        # "LVIII" - 50 + 5 + 1 + 1 + 1
        # "MCMXCIV" - 
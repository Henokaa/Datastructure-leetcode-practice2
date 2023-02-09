class Solution:
    def maximumSwap(self, num: int) -> int:
        digitsMap = {item:ind for ind, item in enumerate(str(num))}
        
        strCopy = list(str(num))
        print(strCopy)
        for ind, char in enumerate(str(num)):
            for d in range(9, int(char), -1):
                digit = str(d)
                if digit in digitsMap and digitsMap[digit] > ind:
                    strCopy[ind], strCopy[digitsMap[digit]] = strCopy[digitsMap[digit]], strCopy[ind]
                    return int("".join(strCopy))
                
        return num
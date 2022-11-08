class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        1 2 4 8
        
        1 2 4 8 16 32
        '''
        output = []
        for h in range(12):
            for m in range(60):
                temp = bin(h) + bin(m)
                if temp.count("1") == turnedOn:
                    output.append((str(h)+":"+str(m).zfill(2)))
                    
        return output
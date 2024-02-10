class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''
        assign l and r
            if outbound just go around
            
        for loop for each element:
            repeat above
        '''
        length = len(code)
        if k > 0:
            total = 0
            l = 0
            for i in range(k):
                total += code[i%length]
                
            r = k-1 % length
        
        
        elif k < 0:
            l = len(code) - abs(k-1)
            r = len(code) - 2
            
            temp = l % length
            total = 0
            print(temp)
            for i in range(abs(k)):
                total += code[temp] 
                temp += 1
                temp = temp % length
        else:
            return [0] * length
                
        answer = []
        for i in range(len(code)):
            total -= code[l]
            l += 1
            l = l % length
            # print("left", total, l, r)
            r += 1
            r = r % length
            total += code[r]
            # print(total)
            answer.append(total)
        return answer
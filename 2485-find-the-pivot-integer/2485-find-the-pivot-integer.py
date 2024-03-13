class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21
        1, 2, 3, 4,   5,  6,  7, 8
        1, 3, 6, 10, 15, 21, 28, 36
                                            36
                    
        '''
        numbers = []
        
        for i in range(1, n + 1):
            numbers.append(i)
        
        for pivot in range(n):
            beforePivot = sum(numbers[:pivot + 1])
            afterPivot = sum(numbers[pivot:])
            
            if beforePivot == afterPivot:
                return pivot + 1
            
        return  -1
            
        
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        '''
        
        '''
        if event1[0] <= event2[0]:
            e1 = event1
            e2 = event2
        else:
            e2 = event1
            e1 = event2
            
        if e1[1] < e2[0]:
            return False
        else:
            if e1[0] > e2[0]:
                return False
            else:
                return True 
            
        
        
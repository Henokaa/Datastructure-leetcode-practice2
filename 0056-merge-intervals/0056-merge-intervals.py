class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        sort with start
        create another array
        stack
        when adding merge
        
        
        '''
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        answer = []
        for x,y in intervals:
            if len(answer) == 0:
                answer.append((x,y))
            else:
                if x <= answer[-1][1]:
                    answer[-1] = (answer[-1][0], max(y,answer[-1][1]))
                else:
                    answer.append((x,y))
        return answer
            
            
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        sort with start
        create another array
        stack
        when adding merge
        
        
        '''
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        print(output)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
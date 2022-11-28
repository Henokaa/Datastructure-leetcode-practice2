class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [73,74,75,71,69,72,76,73]
                ^
        '''
        res = [0] * len(temperatures)
        stack = [] 
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                elem, index = stack.pop()
                res[index] = i - index 
            stack.append((temperatures[i], i))
        return res
            
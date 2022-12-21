class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        if new big pop()
        '''
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            total = 0
            if stack:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    temp = stack[-1][1] - i
                    stack.append((temperatures[i], i))
                    ans[i] = temp
                else:
                    stack.append((temperatures[i], i))
                    ans[i] = 0
                
            else:
                stack.append((temperatures[i], i))
                ans[i] = total
                
        return ans
            
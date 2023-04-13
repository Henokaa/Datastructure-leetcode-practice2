class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        [1,2,3,4,5]
               ^
         
        [4,5,3,2,1]
         ^
        '''
        l = 0
        r = 0
        stack = []
        while l < len(pushed) and r < len(popped):
            while l < len(pushed) and r < len(popped) and pushed[l] != popped[r]:
                stack.append(pushed[l])
                l += 1
                
            if l < len(pushed):
                stack.append(pushed[l])
                
            while l < len(pushed) and r < len(popped) and stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
                
            l += 1
            # if l < len(pushed):
            #     stack.append(pushed[l])
            #     print(stack, l ,r)
        
        print(stack, l, r)
        if l == len(pushed) and r == len(popped):
            return True
        else:
            return False
        
            
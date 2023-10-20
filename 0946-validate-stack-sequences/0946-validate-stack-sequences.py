class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = 0
        r = 0
        stack = []
        while l < len(pushed):
            stack.append(pushed[l])
            while r < len(popped) and stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
                
            l += 1
        
        if l == len(pushed) and r == len(popped):
            return True
        return False
        
        
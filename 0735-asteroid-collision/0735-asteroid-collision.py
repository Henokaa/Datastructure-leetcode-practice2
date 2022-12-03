class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ast = asteroids
        r = 0
    
       
        for i in range(len(ast)):
            while stack and (ast[i] < 0 and stack[-1] > 0) and (abs(stack[-1]) < abs(ast[i])):
                    # print(ast[i], stack[-1])
                    x = stack.pop()
                      
            if stack and (ast[i] < 0 and stack[-1] > 0):
            
                if abs(stack[-1]) > abs(ast[i]):
                    continue
            
                if abs(stack[-1]) == abs(ast[i]):
                    stack.pop()
                    
            else:
                stack.append(ast[i])
        return stack
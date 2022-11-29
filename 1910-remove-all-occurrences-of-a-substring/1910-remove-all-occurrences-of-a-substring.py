class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        arr = list(map(str, part))
        stack = []
        # print(arr)
        for i in range(len(s)):
            
            if len(stack) >= len(arr) - 1 and s[i] == arr[-1]:
                # print(stack)
                if len(arr) == 1:
                    continue
                elem = s[i]
                r = -2 
                i = -1
                while r >= -len(arr)  and arr[r] == stack[i]:
                    r -= 1
                    i -= 1
                
                if r == -len(arr)-1:
                    for x in range(len(arr)-1):
                        stack.pop()
                else:
                    stack.append(elem)
                # print("a", stack)
                
            else:
                stack.append(s[i])
        return "".join(stack)
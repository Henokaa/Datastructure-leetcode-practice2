class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        try testcase - 
        "112"
         1 
        '''
        stack = []
        local_k = 0
        for i in range(len(num)):
            if stack and local_k < k:
                while stack and stack[-1] > num[i] and local_k < k:
                    stack.pop()
                    local_k += 1
                stack.append(num[i])  
            else:
                stack.append(num[i])
            # print(stack)
        
        
        ans = "".join(stack)
        temp = k - local_k
        ans = ans[:len(ans) - temp]
        # print(ans)
        if ans:
            return str(int(ans))
        else:
            return "0"
        
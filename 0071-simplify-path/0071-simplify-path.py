class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        stack
        
        //
        '''
        path = path + "/"
        stack = []
        s = ""
        i = 0
        sign = ""
        while i < len(path):
            if path[i] == "/":
                if s == "..":
                    if stack:
                        stack.pop()
                elif s and s != "." and s != "/":
                    stack.append(s)
                s = ""
                i += 1
            else:
                s += path[i]
                i += 1
                # print(stack, s)
        ans = '/' + '/'.join(stack)
        if ans == "":
            return "/"
        return ans
            
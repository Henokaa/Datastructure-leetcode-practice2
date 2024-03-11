class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        bcabc
        bc
        
        last_dict
        if last_dict >
            pop
        '''
        saved_letter = {}
        for i in range(len(s)):
            saved_letter[s[i]] = i
        
        # print(saved_letter)
        
        r = 0
        stack = []
        visited = set()
        while r < len(s):
            # print(stack)
            if s[r] in visited:
                r += 1
                continue
            if not stack:
                stack.append(s[r])
                visited.add(s[r])
            else:
                if stack[-1] <= s[r]:
                    if s[r] not in visited:
                        stack.append(s[r])
                        visited.add(s[r])
                else:
                    while stack and saved_letter[stack[-1]] > r and stack[-1] > s[r]:
                        last = stack[-1]
                        stack.pop()
                        visited.remove(last)
                    if s[r] not in visited:
                        stack.append(s[r])
                        visited.add(s[r])
            r += 1
            
            
        return "".join(stack)
            
        